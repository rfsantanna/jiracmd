import os
from jira import JIRA


required_variables = ['JIRA_USERNAME', 'JIRA_API_TOKEN', 'JIRA_SERVER']
for var in required_variables:
    if var not in os.environ:
        print(f"ERRROR: Variable {var} is not defined")

jira_client = JIRA(
    server=os.getenv('JIRA_SERVER'),
    basic_auth=(os.getenv('JIRA_USERNAME'), os.getenv('JIRA_API_TOKEN'))
)
