import json
import click
from jiracmd import cli


@click.group(name="issue")
def issue_cli():
    pass

@click.command(name="get")
@click.option('-i', '--issue', required=True)
def issue_get(issue):
    response = cli.jira._get(f'issue/{issue}?expand=changelog')
    print(json.dumps(response.json(), indent=2))

issue_cli.add_command(issue_get)
