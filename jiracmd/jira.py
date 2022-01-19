import requests
import base64

API_VERSION = 3

class JiraAPIClient():
    
    def __init__(self, server, username, token):
        self.base_url = f"https://{server}/rest/api/{API_VERSION}"
        self.headers = self._generate_header(username, token)
        self.session = requests.Session()
        self.session.headers.update(self.headers)


    def _generate_header(self, username, token):
        auth_bytes = f"{username}:{token}".encode('ascii')
        auth_b64 = base64.b64encode(auth_bytes).decode('ascii')
        return {
            "Authorization": f"Basic {auth_b64}",
            "Content-Type": "application/json"
        }

    def _get_endpoint(self, suffix):
        endpoint = f"{self.base_url}/{suffix}"
        return endpoint

    def _get(self, call, **kwargs):
        endpoint = self._get_endpoint(call) 
        return self.session.get(endpoint)

    def _post(self, call, body, **kwargs):
        endpoint = self._get_endpoint(call)
        return self.session.post(endpoint, data=body)

    def _delete(self, call, **kwargs):
        endpoint = self._get_endpoint(call) 
        return self.session.delete(endpoint)


class JiraObject():

    def __init__(self, jira_object):
        self.object = jira_object

    def output_table(self):
        pass

    def output_yaml(self):
        pass
