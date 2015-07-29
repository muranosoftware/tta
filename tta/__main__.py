#!/usr/bin/env python

from __future__ import unicode_literals
import argparse
import operator
from .tt_integration import TTIntegration
from .month_work import GitMonthWork
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
parser.add_argument('-e', '--email',
                    help='Your email in git config',
                    type=str,
                    required=True)
parser.add_argument('-d', '--directory',
                    help='Path to git directory[optional]',
                    default=None)
parser.add_argument('-c', '--category',
                    help=('Time Tracker category, default: Development. Options:\n' +
                          '\n'.join(map(lambda i: '[ {0}\t{1} ]'.format(i[0], i[1]), categories))),
                    choices=list(map(operator.itemgetter(0), categories)),
                    type=int,
                    default=2)


def main():
    options = parser.parse_args()
    tt = TTIntegration(options.user, options.password, category=options.category)
    month_work = GitMonthWork(options.email, options.directory)
    worked_days = get_worked_days()
    commits = month_work.get_last_n_commits(len(worked_days))
    data = zip(worked_days, commits)
    for (current_date, is_working), message in data:
        tt.post_message(current_date, is_working, message)

if __name__ == '__main__':
    main()