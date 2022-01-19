import os
import click
from jiracmd.cli.worklog import worklog_cli
from jiracmd.jira import JiraAPIClient

@click.group()
@click.version_option()
def cli():
    pass

cli.add_command(worklog_cli)

jira = JiraAPIClient(
    os.getenv('JIRA_SERVER'),
    os.getenv('JIRA_USERNAME'),
    os.getenv('JIRA_API_TOKEN')
)
