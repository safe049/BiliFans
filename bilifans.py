import requests
import json
import os
import time

from biliutils import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    asking()
    while True:
        defparams()
        resp = requests_get()
        load_json(resp)
        print_result()
        time.sleep(1)  # 先等待一秒，显示结果
        clear_screen()  # 然后清屏

# output example:
# FOL: 0b110001110110 [3190]
# FAN: 0b11000101101 [1581]
