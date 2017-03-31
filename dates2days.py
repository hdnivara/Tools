#!/usr/bin/python
"""
Calculate the number of days between dates.
"""

import argparse
from datetime import datetime


def __valid_date(date):
    """Check if the given date is in valid format. """
    try:
        return datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        err = "Not a valid date: '{0}'".format(date)
        raise argparse.ArgumentTypeError(err)


def __parse_args():
    """Parse and validate the arguments. """
    parser = argparse.ArgumentParser(
        description="Calculte the number of days between two dates")
    parser.add_argument("startdate", type=__valid_date, nargs=1,
                        help="Start date in YYYY-MM-DD format")
    parser.add_argument("enddate", type=__valid_date, nargs=1,
                        help="End date in YYYY-MM-DD format")
    return vars(parser.parse_args())


def days_between_dates(startdate, enddate):
    """Compute the number of days between start and end dates. """
    return (enddate - startdate).days


def main():
    """Main entrypoint to the program. """
    args = __parse_args()

    startdate = datetime.date(args['startdate'][0])
    enddate = datetime.date(args['enddate'][0])

    num_days = days_between_dates(startdate, enddate)
    print "{0} days".format(num_days)


if __name__ == "__main__":
    main()
