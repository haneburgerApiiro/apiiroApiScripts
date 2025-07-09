#!/usr/bin/env python3
import requests
import json
import configparser
from jsonschema import validate, ValidationError

# Load configuration from file
config = configparser.ConfigParser()
config.read("config.ini")
pat = config.get("AUTH", "MATT_APIIRO_API_TOKEN")

BASE_URL = config.get("API", "BASE_URL")
END_POINT = "/ScmRepositories"
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

def validate_json_data(json_input, schema=None):
    """
    Ingests and validates JSON data.

    Args:
        json_input (str or dict): The JSON data to ingest and validate.
                                   Can be a JSON string or a Python dictionary.
        schema (dict, optional): A JSON schema dictionary for validation.
                                 If provided, the data will be validated against this schema.

    Returns:
        tuple: A tuple containing (validated_data, errors).
               validated_data will be the Python dictionary if validation succeeds,
               otherwise None. errors will be a list of error messages, or empty if no errors.
    """
    errors=[]
    validated_data = None
    try: 
        if isinstance(json_input, str):
            json_input = json.loads(json_input)  # Convert JSON string to Python dict

        if schema:
            validate(instance=json_input, schema=schema)  # Validate against schema
        validated_data = json_input
    except ValidationError as e:
        errors.append(f"Validation error: {e.message}")
    except json.JSONDecodeError as e:
        errors.append(f"JSON decode error: {e.msg}")
    except Exception as e:
        errors.append(f"An unexpected error occurred: {str(e)}")
    return validated_data, errors

# Make the request
response = requests.get(URL, headers=headers, params=params)

if response.status_code == 200:
    try:
        data = response.json()
        jsonData= json.dumps(data, indent=4)
        print(jsonData)
    except requests.exceptions.JSONDecodeError:
        print("⚠️ Response was not valid JSON.")
else:
    print(f"❌ Request failed: {response.status_code}")