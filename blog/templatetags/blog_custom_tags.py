from django.template.defaulttags import register
from blog.models import BlogCategory
from datetime import datetime
from dateutil.relativedelta import *
from collections import deque



@register.simple_tag
def get_categories():
    return BlogCategory.objects.all()



@register.simple_tag
def get_dates():
    today = datetime.now()
    # Get next month and year using relativedelta
    next_month = today + relativedelta(months=+1)
    # How many months do you want to go back?
    num_months_back = 4

    i = 0
    deque_months = deque()

    while i <= num_months_back:
        curr_date = today + relativedelta(months=-i)
        deque_months.appendleft(curr_date.strftime('%B %Y'))
        # print('while : ',deque_months)
        
        if i == num_months_back:
            # deque_months.append(next_month.strftime('%B %Y'))

            i = i+1

    # Convert deque to list
    return deque_months
