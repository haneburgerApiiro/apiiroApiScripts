#!/usr/bin/env python3
from core.auth import get_authenticated_session
from api_modules.Inventory.Applications.main import getApiiroApplications, extractAppKeys, deleteAllApplications
from api_modules.Inventory.SCM_Repositories.main import getApiiroSCMRepositories
from api_modules.Inventory.Organizational_Teams.main import getApiiroTeams

def main():
    json=getApiiroApplications()
    keys=extractAppKeys(json)
    deleteAllApplications(keys)
    print(keys)

    #getApiiroSCMRepositories()
    #getApiiroTeams()

if __name__ == "__main__":
    main()