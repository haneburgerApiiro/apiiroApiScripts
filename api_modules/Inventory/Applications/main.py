#!/usr/bin/env python3

from core.auth import get_authenticated_session
from constants.endpoints import INVENTORY_ENDPOINTS
from utils.jsonValidator import validate_json_data
import json

def getApiiroApplications():
    session=get_authenticated_session()
    applications = INVENTORY_ENDPOINTS["applications"]
    response = session.get(applications, params={"limit": 1})
    if response.status_code == 200:
        try:
            data = response.json()
            jsonData= json.dumps(data, indent=4)
            print(jsonData)
        except session.exceptions.JSONDecodeError:
            print("⚠️ Response was not valid JSON.")