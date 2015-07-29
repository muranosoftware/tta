from __future__ import unicode_literals
import re
from datetime import datetime
from cached_property import cached_property
from requests.auth import HTTPBasicAuth
import requests


selected_option = re.compile(r'<option\s*selected="selected"\s*value="(.+?)"\s*>')


def get_selected_value(html, name):
    regex = '<select\s*name="{0}"[^>]*?>\s*(.+?)\s*</select>'.format(name.replace('$', '\$'))
    sub_html = re.findall(regex, html)[0]
    return selected_option.findall(sub_html)[0]


def get_value(html, name):
    regex = '<input\s[^>]*?name="{0}"[^>]*?value="(.+?)"[^>]*?>'.format(name.replace('$', '\$'))
    return re.findall(regex, html)[0]


def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z


class TTIntegration(object):

    post_url = 'https://tt.muranosoft.com/TimeEntry.aspx'
    holiday_id = 27

    def __init__(self, username, password, category=2):
        self.username = username
        self.password = password
        self.category = category

    @cached_property
    def html(self):
        return requests.post(self.post_url, auth=HTTPBasicAuth(self.username, self.password)).text

    def select_day(self, current_date):
        eventargument = (current_date - datetime(2015, 7, 1)).days + 5660
        data = {
            '__EVENTTARGET': 'ctl00$_content$calDatesSelector',
            '__EVENTARGUMENT': eventargument,
            'ctl00$_content$ScriptManager1':
                'ctl00$_content$ctl00$_content$panelEditFormPanel|ctl00$_content$lbtnAddEntry',
            'ctl00$_content$ddlProjects': get_selected_value(self.html, 'ctl00$_content$ddlProjects'),
            'ctl00$_content$ddlCategories': self.category,
            'ctl00$_content$ucStartTime$ddlHour': 10,
            'ctl00$_content$ucStartTime$ddlMinutes': 0,
            'ctl00$_content$ucEndTime$ddlHour': 18,
            'ctl00$_content$ucEndTime$ddlMinutes': 0,
            'ctl00$_content$ddlUsers': get_selected_value(self.html, 'ctl00$_content$ddlUsers'),
            'RadAJAXControlID': 'ctl00__content_RadAjaxManager1',
            '__VIEWSTATEGENERATOR': get_value(self.html, '__VIEWSTATEGENERATOR'),
            '__VIEWSTATE': get_value(self.html, '__VIEWSTATE'),
            'ctl00$_content$ddlMonths': current_date.month,
            'ctl00$_content$ddlYears': current_date.year,
            'ctl00$_content$ddlDays': current_date.strftime('%d.%m.%Y 0:00:00'),
            'ctl00$_content$tboxDescription': '',
        }
        return requests.post(self.post_url, data, auth=HTTPBasicAuth(self.username, self.password)).text

    def context(self, current_date):
        html = self.select_day(current_date)
        return {
            'ctl00$_content$ScriptManager1':
                'ctl00$_content$ctl00$_content$panelEditFormPanel|ctl00$_content$lbtnAddEntry',
            '__EVENTTARGET': 'ctl00$_content$lbtnAddEntry',
            'ctl00$_content$ddlProjects': get_selected_value(html, 'ctl00$_content$ddlProjects'),
            'ctl00$_content$ddlCategories': self.category,
            'ctl00$_content$ucStartTime$ddlHour': 10,
            'ctl00$_content$ucStartTime$ddlMinutes': 0,
            'ctl00$_content$ucEndTime$ddlHour': 18,
            'ctl00$_content$ucEndTime$ddlMinutes': 0,
            'ctl00$_content$ddlUsers': get_selected_value(html, 'ctl00$_content$ddlUsers'),
            'RadAJAXControlID': 'ctl00__content_RadAjaxManager1',
            '__VIEWSTATEGENERATOR': get_value(html, '__VIEWSTATEGENERATOR'),
            '__VIEWSTATE': get_value(html, '__VIEWSTATE')
        }

    def post_message(self, current_date, is_working, message):
        data = {
            'ctl00$_content$ddlMonths': current_date.month,
            'ctl00$_content$ddlYears': current_date.year,
            'ctl00$_content$ddlDays': current_date.strftime('%d.%m.%Y 0:00:00'),
            'ctl00$_content$tboxDescription': message,
        }
        if not is_working:
            data['ctl00$_content$tboxDescription'] = 'Holiday'
            data['ctl00$_content$ddlCategories'] = self.holiday_id
        post_data = merge_two_dicts(self.context(current_date), data)
        result = requests.post(self.post_url, post_data, auth=HTTPBasicAuth(self.username, self.password))
        print('{0} - {1} : {2} - {3}'.format(
            result,
            current_date,
            post_data['ctl00$_content$ddlCategories'],
            post_data['ctl00$_content$tboxDescription']))