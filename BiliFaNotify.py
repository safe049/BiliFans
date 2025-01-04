import requests
import json
import os
import time

from biliutils import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_json(response):
    global following_count, follower_count, follower_binary_count, following_binary_count
    data = json.loads(response.text)
    # 提取 following 和 follower 的数字
    following_count = data["data"]["following"]
    follower_count = data["data"]["follower"]
    following_binary_count = bin(data["data"]["following"])
    follower_binary_count = bin(data["data"]["follower"])
    return following_count, follower_count,follower_binary_count,following_binary_count

def notify_result():
    os.system(f'notify-send "BiliFans" "FOL: {following_binary_count} [{following_count}]\nFAN: {follower_binary_count} [{follower_count}]"')

if __name__ == "__main__":
    asking()
    while True:
        defparams()
        resp = requests_get()
        load_json(resp)
        notify_result()
        time.sleep(1)  # 先等待一秒，显示结果
        clear_screen()  # 然后清屏

# output example:
# FOL: 0b110001110110 [3190]
# FAN: 0b11000101101 [1581]
