from core.config import get_config

config = get_config()
BASE_URL = config.get("base_url")

ENDPOINTS = {
    "application_groups": f"{BASE_URL}/ApplicationGroups",
    "scm_repositories": f"{BASE_URL}/ScmRepositories"
}