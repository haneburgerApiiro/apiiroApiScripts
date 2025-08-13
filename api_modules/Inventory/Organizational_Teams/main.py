from core.auth import get_authenticated_session
from constants.endpoints import INVENTORY_ENDPOINTS
import json

def getApiiroTeams():
    session=get_authenticated_session()
    teams = INVENTORY_ENDPOINTS["teams"]
    response = session.get(teams, params={"limit": 50})
    if response.status_code == 200:
        try:
            data = response.json()
            jsonData = json.dumps(data, indent=4)
            print(jsonData)
        except session.exceptions.JSONDecodeError:
            print("⚠️ Response was not valid JSON.")