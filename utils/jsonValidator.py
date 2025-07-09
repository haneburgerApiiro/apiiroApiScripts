import json
from jsonschema import validate, ValidationError

def validate_json_data(json_input, schema=None):
    """
    Validates JSON data and returns a status indicator and message.

    Args:
        json_input (str or dict): The JSON data to validate (as a string or dictionary).
        schema (dict, optional): A JSON Schema dictionary to validate against.

    Returns:
        tuple: A tuple containing (status_emoji, message).
               - status_emoji: '✅' if valid, '❌' if not.
               - message: 'JSON is valid.' or a detailed reason why it's not.
    """
    try:
        if isinstance(json_input, str):
            json_input = json.loads(json_input)

        if schema:
            validate(instance=json_input, schema=schema)

        return '✅', 'JSON is valid.'

    except json.JSONDecodeError as e:
        return '❌', f'Invalid JSON format: {e.msg}'
    except ValidationError as e:
        return '❌', f'Schema validation error: {e.message}'
    except Exception as e:
        return '❌', f'Unexpected error: {str(e)}'