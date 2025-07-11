from core.config import get_config

config = get_config()
BASE_URL = config.get("base_url")

INVENTORY_ENDPOINTS = {
    "applicationGroups": f"{BASE_URL}/applicationGroups",
    "applicationProfiles": f"{BASE_URL}/applications/profiles",
    "applications": f"{BASE_URL}/applications",
    "inventory": f"{BASE_URL}/inventory",
    "teams": f"{BASE_URL}/teams",
    "repositories": f"{BASE_URL}/repositories", #this is a V2 endpoint ~ need to refactor constants/endpoints.py
    "scm_repositories": f"{BASE_URL}/ScmRepositories"
    }

SETTINGS_ENDPOINTS = {
    "auditLogs": f"{BASE_URL}/auditLogs"
}

INTEGRATIONS_ENDPOINTS = {
    "build_scans": f"{BASE_URL}/buildScan/builds",
    "managed_semgrep": f"{BASE_URL}/semgrepConfiguration",
    "pull_requests": f"{BASE_URL}/pullRequests"
}