from __future__ import unicode_literals
from datetime import date, datetime
from functools import partial
import operator
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, DAILY, MO, TU, WE, TH, FR
import requests


calened_url = 'http://basicdata.ru/api/json/calend/'

date_format = "%Y-%m-%d"


def mark_holidays(cal_dates, current_date):
    is_working = (cal_dates
                  .get(current_date.year, {})
                  .get(current_date.month, {})
                  .get(current_date.day, {})
                  .get('isWorking', 0))
    return current_date, not is_working


def get_worked_days(start_date=None, end_date=None):
    if start_date is None:
        start_date = date.today()+relativedelta(day=1)
    else:
        start_date = datetime.strptime(start_date, date_format).date()
    if end_date is None:
        end_date = date.today()+relativedelta(months=+1, day=1) + relativedelta(days=-1)
    else:
        end_date = datetime.strptime(end_date, date_format).date()
    response = requests.get(calened_url)
    cal_dates = response.json()
    dates = rrule(DAILY,
                  dtstart=start_date,
                  until=end_date,
                  byweekday=(MO, TU, WE, TH, FR))
    usual_worked_days = list(map(partial(mark_holidays, cal_dates), dates))
    today = date.today()
    days = (cal_dates.get(today.year, {}).get(today.month, {}))
    worked_dates = [(datetime(today.year, today.month, day), True) for day in days if days.get(day).get('isWorking') == 0]
    return list(sorted(usual_worked_days + worked_dates, key=operator.itemgetter(0)))