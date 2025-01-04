import requests
import json
import os

def asking():
    global vmidinput  # 将 global 声明放在赋值之前
    vmidinput = input("请输入账号ID: ")
    return vmidinput

def defparams():
    global params, headers  
    params = {"vmid": vmidinput, "jsonp": "jsonp"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

def requests_get():
    response = requests.get("https://api.bilibili.com/x/relation/stat", params=params, headers=headers)
    return response

def load_json(response):
    global following_count, follower_count, follower_binary_count, following_binary_count
    data = json.loads(response.text)
    # 提取 following 和 follower 的数字
    following_count = data["data"]["following"]
    follower_count = data["data"]["follower"]
    following_binary_count = bin(data["data"]["following"])
    follower_binary_count = bin(data["data"]["follower"])
    return following_count, follower_count,follower_binary_count,following_binary_count

def print_result():
    print(f"FOL: {following_binary_count} [{following_count}]")
    print(f"FAN: {follower_binary_count} [{follower_count}]")