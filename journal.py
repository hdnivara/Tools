#!/usr/bin/env python

"""
Create a journal with date and days for given month.
"""

import argparse
import calendar
from datetime import datetime


def __parse_args():
    """ Parse and verify user arguments. """
    parser = argparse.ArgumentParser(description='Print journal dates')
    parser.add_argument('-m', metavar='MM', dest='month', type=int,
                        required=False,
                        help="print dates of given month; default = current month")
    parser.add_argument('-y', metavar="YYYY", dest="year", type=int,
                        required=False,
                        help="print dates of given year; default = current year")

    args = parser.parse_args()

    if args.month is not None and (args.month < 1 or args.month > 12):
        err = "Invalid month. Valid months are 1-12."
        raise parser.error(err)

    return args


def print_journal(start_day, month, year):
    """ Print date and day in ISO 8601 format. """
    print start_day, month, year
    cal = calendar.Calendar()
    print '=' * 80

    for date in sorted((date for date in cal.itermonthdates(year, month))):
        if not date.month == month:
            continue

        if date.day < start_day:
            continue

        print date, date.strftime(' %a'), '\n'


def main():
    """ Entrypoint to the program. """
    args = vars(__parse_args())
    today = datetime.now()

    if args['month'] is None and args['year'] is None:
        args['day'] = today.day
    else:
        args['day'] = 1

    if args['month'] is None:
        args['month'] = today.month

    if args['year'] is None:
        args['year'] = today.year

    print_journal(args['day'], args['month'], args['year'])


if __name__ == "__main__":
    main()
