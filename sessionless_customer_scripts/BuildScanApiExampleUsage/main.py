#!/usr/bin/env python3
import requests
import json
import os
import configparser

API_BASE_URL = "https://app-staging.apiiro.com/rest-api/v1"
POST_BUILD_SCAN_ENDPOINT = f"{API_BASE_URL}/buildScan/builds"
GET_RESULTS_ENDPOINT_TEMPLATE = f"{API_BASE_URL}/buildScan/{{build_id}}/results"

config = configparser.ConfigParser()
config.read('../../config.ini')

API_TOKEN = config.get('AUTH', 'MATT_APIIRO_API_TOKEN')

COMMIT_SHA_1="b57d0faa3032db8cd80b35a2aafeae20b4e191ad"
COMMIT_SHA_2="0d407c5c618e3c0b6bb5ff48c40bd4b8cc1f0c5b"

REPO_URL = "https://github.com/haneburgerApiiro/buildScanAPIv1-react"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}

def create_build_scan(commit_sha: str, repository_url: str) -> str:
    payload = {
        "commitSha": commit_sha,
        "repositoryUrl": repository_url
    }

    response = requests.post(POST_BUILD_SCAN_ENDPOINT, headers=HEADERS, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"Failed to create build scan: {response.status_code} - {response.text}")
    


def get_build_scan_results(build_id: str) -> dict:
    url = GET_RESULTS_ENDPOINT_TEMPLATE.format(build_id=build_id)
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch scan results: {response.status_code} - {response.text}")

    print(f"Scan results fetched for build ID: {build_id}")
    return response.json()

if __name__ == "__main__":
    buildID='yoxSMhOdq0O9nIIax4vAhg'
    print(json.dumps(get_build_scan_results(buildID)))
