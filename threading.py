# without threading
import time
start = time.perf_counter()

def do_something():
  print('sleeping for 1 second...')
  time.sleep(1)
  print('Done sleeping')
  
do_something()
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')


#with threading
import threading
import time
start = time.perf_counter()

def do_something():
  print('sleeping for 1 second...')
  time.sleep(1)
  print('Done sleeping')
  
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
