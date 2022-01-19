import json
import click
from jiracmd import cli
from datetime import datetime


@click.group(name="issue")
def issue_cli():
    pass

@click.command(name="get")
@click.option('-i', '--issue', required=True)
def issue_get(issue):
    response = cli.jira._get(f'issue/{issue}?expand=changelog')
    print(json.dumps(response.json(), indent=2))

@click.command(name="list")
@click.option('--me', is_flag=True, default=True)
@click.option('-t', '--issue-type', default=None)
def issue_list(me, issue_type):
    type_query = ""
    if issue_type:
        type_query = f"and issueType={issue_type}"
    jql = f"assignee=currentuser() {type_query}"
    response = cli.jira._get(f'search?maxResults=100&jql={jql}')
    issues = response.json()['issues']
    print(f"{'Issue':12}{'Type':12}{'Updated':12}{'Summary'}")
    print(f"{'-----':12}{'----':12}{'-------':12}{'-------'}")
    for i in issues:
        key = i['key']
        summary = i['fields']['summary']
        updated = datetime.strptime(i['fields']['updated'], '%Y-%m-%dT%H:%M:%S.%f%z')
        i_type = i['fields']['issuetype']['name']
        date = str(updated.date())
        print(f"{key:12}{i_type:12}{date:12}{summary[:65]}...")

issue_cli.add_command(issue_get)
issue_cli.add_command(issue_list)



# jira/rest/api/2/search?jql=assignee=currentuser()
