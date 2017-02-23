'''
Write a function get_age(birth_date, current_date=None) which returns the age of a person on the current date

Birth date will be the datetime.date object.

Current date will also be a datetime.date object, but should be optional. If the current date is ommited then default
to the current date in UTC.
'''

import datetime
import time
from datetime import date

def get_age(birth_date, current_date=None):
    today = date.today()


    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
print (get_age(1978))

