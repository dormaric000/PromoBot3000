import requests
import time
import os
import json
from datetime import datetime
import random


try:
    with open('Config.json', 'r') as file:
        config = json.load(file)
        webhook_url = config['webhook_url']
except FileNotFoundError:
    print("Config.json file not found. Please redownload the project.")
    time.sleep(5)
    exit(1)

if webhook_url == "":
    print("Webhook URL not found in Config.json. Please fill in the webhook URL.")
    time.sleep(5)
    exit(1)


try:
    print("Bot is running.")
    while True:
        if config['use_random_messages']:
            data = random.choice(config['random_messages'])
            response = requests.post(webhook_url, json=data)
        else:
            data = config['default_message']
            response = requests.post(webhook_url, json=data)

        if response.status_code == 204:
            print(f"Message sent successfully at {datetime.now().strftime('%H:%M:%S.%f')[:-4]}. Status code: {response.status_code}")
        else:
            print(f"Failed to send message at {datetime.now().strftime('%H:%M:%S.%f')[:-4]}. Status code: {response.status_code}")

        print(f"Waiting for {config.get('delay', 60)} seconds")
        delay = config.get('delay', 60)
        time.sleep(delay)        
except Exception as e:
    print(f"Error: {e}")