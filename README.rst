tta - Time Tracker Autocompleter for Muranosoft
===============================================

.. image:: https://img.shields.io/pypi/v/tta.svg
    :target: https://pypi.python.org/pypi/tta
    :alt: Latest PyPI version

Time Tracker Autocompleter for Muranosoft

This tool automatically fill out Time Tracker with messages from your git log.

Installation:
-------------

Install Python: `OSX <http://docs.python-guide.org/en/latest/starting/install/osx/>`_. `Windows <http://docs.python-guide.org/en/latest/starting/install/win/>`_. `Linux <http://docs.python-guide.org/en/latest/starting/install/linux/>`_.

Install **tta** (*run console command*):

.. code::
    
    pip install tta

Usage:
------

Type this command in console (in folder with your git repo):

.. code::

    tta -u user -p qwerty -e gmail@gmail.com

* user - Your username in Time Tracker
* qwerty - Your password in Time Tracker
* gmail@gmail.com - Your email in git config

Options:
--------


+---------------------------+----------------------------------------------+
| Option                    | Description                                  |
+======+====================+==============================================+
| *-u* | *--user*           | Time Tracker username                        |
+------+--------------------+----------------------------------------------+
| *-p* | *--password*       | Time Tracker password                        |
+------+--------------------+----------------------------------------------+
| *-e* | *--email*          | Your email in git config                     |
+------+--------------------+----------------------------------------------+
| *-d* | *--directory*      | Path to git directory                        |
+------+--------------------+----------------------------------------------+
|      | *--start_date*     | Start date of period (EX: 2015-8-27)         |
|      |                    | *Default: first day of current month*        |
+------+--------------------+----------------------------------------------+
|      | *--end_date*       | End date of period (EX: 2015-8-29)           |
|      |                    | *Default: last day of current month*         |
+------+--------------------+----------------------------------------------+
|      | *--start_work_day* | Hour of start working day. Default: *10*     |
+------+--------------------+----------------------------------------------+
|      | *--end_work_day*   | Hour of end working day. Default: *18*       |
+------+--------------------+----------------------------------------------+
| *-c* | *--category*       | Time Tracker category, default: Development. |
|      |                    |                                              |
|      |                    +----------------------------------------------+
|      |                    | **Categories:**                              |
|      |                    +----+-----------------------------------------+
|      |                    | ID | Name                                    |
|      |                    +----+-----------------------------------------+
|      |                    | 17 | Client Support                          |
|      |                    +----+-----------------------------------------+
|      |                    | 12 | Code Review                             |
|      |                    +----+-----------------------------------------+
|      |                    | 2  | Development                             |
|      |                    +----+-----------------------------------------+
|      |                    | 4  | Documenting                             |
|      |                    +----+-----------------------------------------+
|      |                    | 15 | Graphic Design                          |
|      |                    +----+-----------------------------------------+
|      |                    | 27 | Holiday                                 |
|      |                    +----+-----------------------------------------+
|      |                    | 29 | HR                                      |
|      |                    +----+-----------------------------------------+
|      |                    | 14 | Infrastructure                          |
|      |                    +----+-----------------------------------------+
|      |                    | 28 | Marketing                               |
|      |                    +----+-----------------------------------------+
|      |                    | 7  | Meeting                                 |
|      |                    +----+-----------------------------------------+
|      |                    | 8  | Miscellaneous                           |
|      |                    +----+-----------------------------------------+
|      |                    | 30 | Office Management                       |
|      |                    +----+-----------------------------------------+
|      |                    | 35 | Overtime leave                          |
|      |                    +----+-----------------------------------------+
|      |                    | 9  | Project Management                      |
|      |                    +----+-----------------------------------------+
|      |                    | 10 | Quality Assurance/Testing               |
|      |                    +----+-----------------------------------------+
|      |                    | 3  | Requirement Analysis                    |
|      |                    +----+-----------------------------------------+
|      |                    | 6  | Research                                |
|      |                    +----+-----------------------------------------+
|      |                    | 25 | Sick                                    |
|      |                    +----+-----------------------------------------+
|      |                    | 31 | Vacation non-paid                       |
|      |                    +----+-----------------------------------------+
|      |                    | 26 | Vacation paid                           |
+------+--------------------+----+-----------------------------------------+


`tta` was written by `Kirill Ermolov <erm0l0v@ya.ru>`_.
