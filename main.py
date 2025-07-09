#!/usr/bin/env python3
import requests
import json
import configparser
import warnings

# Load configuration from file
config = configparser.ConfigParser()
config.read("config.ini")
pat = config.get("AUTH", "MATT_APIIRO_API_TOKEN")

BASE_URL = "https://app.apiiro.com/v1"
END_POINT = "/scm-repositories"
URL = f"{BASE_URL}{END_POINT}"

# Headers with Bearer Token
headers = {
    "Authorization": f"Bearer {pat}",
    "Accept": "application/json"
}

# Optional query parameters (e.g., filter, pagination)
params = {
    "limit": 50
}

# Make the request
response = requests.get(URL, headers=headers, params=params)

if response.status_code == 200:
    try:
        data = response.json()
        print("Parsed JSON:", data)
    except requests.exceptions.JSONDecodeError:
        print("⚠️ Response was not valid JSON.")
else:
    print(f"❌ Request failed: {response.status_code}")