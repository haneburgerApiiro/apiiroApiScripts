import requests
from core.config import get_config

def get_authenticated_session():
    config = get_config()
    auth_token = config.get("auth_token")
    base_url = config.get("base_url")

    # Create a session
    session = requests.Session()
    
    # Setting the base URL for the session
    session.base_url = base_url
    
    # Set the headers with Bearer Token
    session.headers.update({
        "Authorization": f"Bearer {auth_token}",
        "Accept": "application/json"
    })
    
    return session