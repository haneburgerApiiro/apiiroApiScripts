#!/usr/bin/env python3
from core.auth import get_authenticated_session
from constants.endpoints import ENDPOINTS
from utils.jsonValidator import validate_json_data

import json

def main():
    session = get_authenticated_session()
    scmRepositories_url = ENDPOINTS["scm_repositories"]
    response = session.get(scmRepositories_url, params={"limit": 50})
    
    if response.status_code == 200:
        try:
            data = response.json()
            jsonData= json.dumps(data, indent=4)
            print(jsonData)
            print(validate_json_data(jsonData, schema=None))
        except session.exceptions.JSONDecodeError:
            print("⚠️ Response was not valid JSON.")
if __name__ == "__main__":
    main()