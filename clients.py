import requests
from typing import Any, Dict, List
from config import BASE_URL, API_TOKEN


class BaseClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {
            'accept': 'application/json',
            'x-access-token': API_TOKEN
        }

    def get_cluster_id(self) -> str:
        response = requests.get(
            f"{self.base_url}/api/v1/clusters",
            headers=self.headers,
            verify=False
        )
        response.raise_for_status()
        return response.json().get("data")[0].get("cluster_id")

    def get_image_digest(self, cluster_id: str, application_name: str) -> str:
        params = {
            'clusterId': cluster_id,
            'applicationName': application_name,
            'usedImages': 'true'
        }
        response = requests.get(
            f"{self.base_url}/api/v1/images/runtime",
            headers=self.headers,
            params=params,
            verify=False
        )
        response.raise_for_status()
        return response.json()[0].get("digest")

    def get_image_id(self, digest: str) -> str:
        params = {'digest': digest}
        response = requests.get(
            f"{self.base_url}/api/v1/sbom/by-digest",
            headers=self.headers,
            params=params,
            verify=False
        )
        response.raise_for_status()
        return response.json()[0].get("id")

    def get_report(self, image_id: str) -> List[Dict[str, Any]]:
        params = {'id': image_id}
        response = requests.get(
            f"{self.base_url}/api/v1/sbom/components",
            headers=self.headers,
            params=params,
            verify=False
        )
        response.raise_for_status()
        return response.json()
