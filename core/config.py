from configparser import ConfigParser

def get_config() -> dict:
    parser = ConfigParser()
    parser.read("config.ini")
    return {
        "auth_token": parser.get("AUTH", "MATT_APIIRO_API_TOKEN"),
        "base_url": parser.get("API", "BASE_URL")
    }