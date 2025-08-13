from core.auth import get_authenticated_session
from constants.endpoints import INVENTORY_ENDPOINTS
import json

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