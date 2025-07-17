#!/usr/bin/env python3
import pandas as pd
import requests
import json

EXCEL_FILE_PATH = 'dummy.xlsx'
ENDPOINT_URL = "https://app.apiiro.com/rest-api/v1/applicationGroups" 
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer [apiiro_user_token]" # Replace with your actual API token
}

def readGroupNames(file_path):
    try:
        df = pd.read_excel(file_path)
        group_names = df['Group Name Value'].tolist()
        return group_names
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def createApplicationGroup(group_names):
    for name in group_names:
        payload = {
            "applications": ["APP_ID"], # Replace with existing application ID, you can delete later
            "name": name,
            "pointsOfContact": [],
            "tags": []
        }

        response = requests.post(ENDPOINT_URL, headers=HEADERS, data=json.dumps(payload))
        print(f"Creating Group: {name}")
        print("Status Code:", response.status_code)
        try:
            response_data = response.json()
            print("Response Data:", json.dumps(response_data, indent=4))
        except requests.exceptions.JSONDecodeError:
            print("Response was not valid JSON.")

if __name__ == "__main__":
    group_names = readGroupNames(EXCEL_FILE_PATH)
    if group_names:
        createApplicationGroup(group_names)
    else:
        print("No group names found in the Excel file.")