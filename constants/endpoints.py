from core.config import get_config

config = get_config()
BASE_URL = config.get("base_url")

ENDPOINTS = {
    "applications": f"{BASE_URL}/applications",
    "scm_repositories": f"{BASE_URL}/ScmRepositories",
    "teams": f"{BASE_URL}/teams"
}