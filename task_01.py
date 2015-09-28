#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module gives you the current date"""


# Import sys libs
import datetime

CURDATE = None


def get_current_date():
    """
    This function gives you the current date.

    Args:
        date (int): the current date.

    Returns:
        int: returns date in number format

    Examples:

        >>> task_01.get_current_date()
        datetime.date(2015, 1, 1)

    """
    date = datetime.date.today()
    return date
