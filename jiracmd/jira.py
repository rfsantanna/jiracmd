import requests

API_VERSION = 3

class JiraAPIClient():
    
    def __init__(self, server, username, token):
        self.base_url = f"https://{server}/rest/api/{API_VERSION}"
        self.headers = self._generate_header(username, token)

    def _generate_header():
        b64_auth = f"{username}:{token}"
        return {
            "Authorization": f"Basic {b64_auth}",
            "Content-Type": "application/json"
        }

    def _get(self, call, **kwargs):
        pass

    def _post(self, call, body, **kwargs):
        endpoint = f"{self.base_url}/{call}"
        requests.post()

