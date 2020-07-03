#!/usr/bin/env python

from __future__ import unicode_literals
import argparse
import operator
from .tt_integration import TTIntegration
from .worked_days import get_worked_days


categories = (
    (17, 'Client Support'),
    (12, 'Code Review'),
    (2, 'Development'),
    (4, 'Documenting'),
    (15, 'Graphic Design'),
    (27, 'Holiday'),
    (29, 'HR'),
    (14, 'Infrastructure'),
    (28, 'Marketing'),
    (7, 'Meeting'),
    (8, 'Miscellaneous'),
    (30, 'Office Management'),
    (35, 'Overtime leave'),
    (9, 'Project Management'),
    (10, 'Quality Assurance/Testing'),
    (3, 'Requirement Analysis'),
    (6, 'Research'),
    (25, 'Sick'),
    (31, 'Vacation non-paid'),
    (26, 'Vacation paid')
)


parser = argparse.ArgumentParser(description='Time Tracker Autocompleter for Muranosoft.')
parser.add_argument('-u', '--user',
                    help='Time Tracker username',
                    type=str,
                    required=True)
parser.add_argument('-p', '--password',
                    help='Time Tracker password',
                    type=str,
                    required=True)
parser.add_argument('-m', '--message',
                    help='Time Tracker message',
                    type=str,
                    required=True)
parser.add_argument('-c', '--category',
                    help=('Time Tracker category, default: Development. Options:\n' +
                          '\n'.join(map(lambda i: '[ {0}\t{1} ]'.format(i[0], i[1]), categories))),
                    choices=list(map(operator.itemgetter(0), categories)),
                    type=int,
                    default=2)
parser.add_argument('--start_date',
                    help='Start date of period, Default: first day of current month',
                    type=str,
                    default=None)
parser.add_argument('--end_date',
                    help='End date of period, Default: last day of current month',
                    type=str,
                    default=None)
parser.add_argument('--start_work_day',
                    help='Hour of start working day. Default: 10',
                    type=int,
                    default=10)
parser.add_argument('--end_work_day',
                    help='Hour of end working day. Default: 18',
                    type=int,
                    default=18)


def main():
    options = parser.parse_args()
    tt = TTIntegration(options.user,
                       options.password,
                       options.category,
                       options.start_work_day,
                       options.end_work_day)
    
    worked_days = get_worked_days(options.start_date, options.end_date)
    for current_date, is_working in worked_days:
        tt.post_message(current_date, is_working, options.message)

if __name__ == '__main__':
    main()