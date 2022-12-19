import time
import threading
import requests
import multiprocessing
import concurrent.futures
start_at = time.perf_counter()
# or:
# start_at = time.time()

# def do_something(name):
#     print(f'{name}- started')
#     time.sleep(3)
#     print(f'{name}- finished')


# t1 = threading.Thread(target=do_something, args=['Function1'])
# t2 = threading.Thread(target=do_something, args=['Function2'])


# t1.start()
# t2.start()

# t1.join()
# t2.join()


# def download_image (number):
#     r = requests.get('https://picsum.photos/200/300')
#     with open (f'images/image{number}.png', 'wb') as f:
#         f.write(r.content)
#     print(f'{number}.image')
    
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = executor.map(download_image, range(100))


# threads = []
# for i in range(1,6):
#     threads.append(threading.Thread(target=download_image, args=[i])) 


# for thread in threads:
#     thread.start()

# for thread in threads:
#     thread.join()
    

# finish_at = time.perf_counter()
# print(f'Functions end in {finish_at-start_at} sec.')


from datetime import datetime, timedelta
from dateutil.relativedelta import *
from collections import deque

today = datetime.now()
# Get next month and year using relativedelta
next_month = today + relativedelta(months=+1)
# How many months do you want to go back?
num_months_back = 4

i = 1
deque_months = deque()
print(deque_months)

while i <= num_months_back:
    curr_date = today + relativedelta(months=-i)
    print('curr_date', curr_date)
    deque_months.appendleft(curr_date.strftime('%B %Y'))
    # print('while : ',deque_months)


    if i == num_months_back:
        # deque_months.append(next_month.strftime('%B %Y'))

        i = i+1

# Convert deque to list
print(list(deque_months))