import requests
import os
import sys
import time
import json
import datetime
from GetIp import *


url = 'https://pastebin.com/raw/Nb16PwK8' # url from where to read the licenses
webhook_url = 'https://discord.com/api/webhooks/1139007996685467790/Z3PDG-KjjeSR0JYoJ2VSQub7nHY22xLU6Yq-W0GZq8Ar_mqT4sirCaq2xGJvNPOvDyNZ' # discord webhook url
ipv4 = get_public_ip()
response = requests.get(url)
validkeys = []


# Gattering the valid keys
for line in response.iter_lines(): # for each line in the response append to validkeys
    if line:
        validkeys.append(line.decode("utf-8"))


# Starting the authentications
LicenseKey = input('[+] Enter License Key: ')
if LicenseKey in validkeys: # Grant Access if the license is valid

    os.system('cls')
    print('[+] Valid License Key.')
    print('[+] Access Granted.')

    curr_time = datetime.datetime.now()
    message_content = {
        "content": "Successful login attempt from " + ipv4 + " at " + str(curr_time)
    }
    json_data = json.dumps(message_content)
    webhook_log = requests.post(webhook_url, data=json_data, headers={'Content-Type': 'application/json'})

    time.sleep(3)
    pass
else: # deny access if the license isn't valid and exit the program
    os.system('cls')
    print('[+] Invalid License Key.')
    print('[+] Access Denied.')

    curr_time = datetime.datetime.now()
    message_content = {
        "content": "Login attempt failed from " + ipv4 + " at " + str(curr_time)
    }
    json_data = json.dumps(message_content)
    webhook_log = requests.post(webhook_url, data=json_data, headers={'Content-Type': 'application/json'})

    time.sleep(3)
    sys.exit()


# post authentication
os.system('cls')
print('[1] Option 1\n')
print('[2] Option 2\n')
print('[3] Exit\n')

option = input('[+] Enter your option: ')

if option == '1':
    pass
elif option == '2':
    pass
elif option == '3':
    sys.exit()