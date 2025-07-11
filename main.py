#!/usr/bin/env python3
from core.auth import get_authenticated_session
from constants.endpoints import INVENTORY_ENDPOINTS
from utils.jsonValidator import validate_json_data
import json

def getApiiroApplications():
    session=get_authenticated_session()
    applications = INVENTORY_ENDPOINTS["applications"]
    response = session.get(applications, params={"limit": 50})
    if response.status_code == 200:
        try:
            data = response.json()
            jsonData= json.dumps(data, indent=4)
            print(jsonData)
        except session.exceptions.JSONDecodeError:
            print("⚠️ Response was not valid JSON.")

def getApiiroSCMRepositories():
    session=get_authenticated_session()
    scm_repositories = INVENTORY_ENDPOINTS["scm_repositories"]
    response = session.get(scm_repositories, params={"limit": 50})
    if response.status_code == 200:
        try:
            data = response.json()
            jsonData= json.dumps(data, indent=4)
            print(jsonData)
        except session.exceptions.JSONDecodeError:
            print("⚠️ Response was not valid JSON.")

def getApiiroTeams():
    session=get_authenticated_session()
    teams = INVENTORY_ENDPOINTS["teams"]
    response = session.get(teams, params={"limit": 50})
    if response.status_code == 200:
        try:
            data = response.json()
            jsonData= json.dumps(data, indent=4)
            print(jsonData)
            print(validate_json_data(jsonData, schema=None))
        except session.exceptions.JSONDecodeError:
            print("⚠️ Response was not valid JSON.")

def main():
    #getApiiroApplications()
    #getApiiroSCMRepositories()
    getApiiroTeams()
    # Add more function calls here as needed

if __name__ == "__main__":
    main()