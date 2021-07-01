from __future__ import unicode_literals
from datetime import date, datetime
from functools import partial
import operator
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, DAILY, MO, TU, WE, TH, FR
import requests


calendService = 'https://isdayoff.ru/'

date_format = "%Y-%m-%d"


def workingDaysFilter(dt):
    formattedDate = dt.strftime(date_format)
    requestUrl = calendService + formattedDate
    response = requests.get(requestUrl)
    print(requestUrl + " " + response.text)
    if (response.text=='0'):
        return True
    else:
        return False


def get_worked_days(start_date=None, end_date=None):
    if start_date is None:
        start_date = date.today()+relativedelta(day=1)
    else:
        start_date = datetime.strptime(start_date, date_format).date()
    if end_date is None:
        end_date = date.today()+relativedelta(months=+1, day=1) + relativedelta(days=-1)
    else:
        end_date = datetime.strptime(end_date, date_format).date()
    
    dates = rrule(DAILY,
                  dtstart=start_date,
                  until=end_date)

    datesFiltered = list(filter(lambda x: workingDaysFilter(x), dates))
    # workingDays = list(map(lambda x: x.strftime(date_format), datesFiltered))

    return datesFiltered