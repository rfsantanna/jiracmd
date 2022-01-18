import os
import click
from jiracmd import jira_client
from jiracmd.worklog import cli_worklog

@click.group()
@click.version_option()
def cli():
    pass


cli.add_command(cli_worklog)

if __name__ == "__main__":
    cli()
