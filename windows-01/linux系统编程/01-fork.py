import os
import time
ret = os.fork()
if ret==0:
    while True:
        print("11111111")
        time.sleep(1)
else:
    while True:
        print("2222222")
        time.sleep(1)

