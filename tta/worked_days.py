from __future__ import unicode_literals
from datetime import date, datetime
from functools import partial
import operator
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, DAILY, MO, TU, WE, TH, FR
import requests


calend_url = 'http://basicdata.ru/api/json/calend/'


def mark_holidays(cal_dates, current_date):
    is_working = (cal_dates
                  .get(current_date.year, {})
                  .get(current_date.month, {})
                  .get(current_date.day, {})
                  .get('isWorking', 0))
    return current_date, not is_working


def get_worked_days():
    response = requests.get(calend_url)
    cal_dates = response.json()
    dates = rrule(DAILY,
                  dtstart=date.today()+relativedelta(day=1),
                  until=date.today()+relativedelta(months=+1, day=1) + relativedelta(days=-1),
                  byweekday=(MO, TU, WE, TH, FR))
    usual_worked_days = list(map(partial(mark_holidays, cal_dates), dates))
    today = date.today()
    days = (cal_dates.get(today.year, {}).get(today.month, {}))
    worked_dates = [(datetime(today.year, today.month, day), True) for day in days if days.get(day).get('isWorking') == 0]
    return list(sorted(usual_worked_days + worked_dates, key=operator.itemgetter(0)))