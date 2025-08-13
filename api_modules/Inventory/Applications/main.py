from core.auth import get_authenticated_session
from constants.endpoints import INVENTORY_ENDPOINTS
import json

def getApiiroApplications():
    session=get_authenticated_session()
    applications = INVENTORY_ENDPOINTS["applications"]
    response = session.get(applications, params={"limit": 50})
    if response.status_code == 200:
        try:
            data = response.json()
            jsonData= json.dumps(data, indent=4)
        except session.exceptions.JSONDecodeError:
            print("⚠️ Response was not valid JSON.")
    return jsonData

def extractAppKeys(api_response_str):
    api_response = json.loads(api_response_str)
    try:
        return [item['key'] for item in api_response.get('items', [])]
    except json.JSONDecodeError:
        print("⚠️ Error decoding JSON response.")
        return []

def deleteAllApplications(keys: list[str]):
    session = get_authenticated_session()
    applications = INVENTORY_ENDPOINTS["applications"]
    for key in keys:
        response = session.delete(f"{applications}/{key}")
        if response.status_code == 200:
            print(f"Application with key {key} deleted successfully.")
        else:
            print(f"Failed to delete application with key {key}. Status code: {response.status_code}")
