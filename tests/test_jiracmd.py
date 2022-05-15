import os
from click.testing import CliRunner
from jiracmd.cli import cli

os.environ['JIRA_SERVER'] = "jiratest.atlassian.net"
os.environ['JIRA_USERNAME'] = "jiratester@jiratest.com"
os.environ['JIRA_SERVER'] = "alskdjalksdjalksjdalsC"


def test_version_flag():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert result.output.startswith("cli, version ")

def test_version_output():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--version"])
        assert result.output.startswith("cli, version ")
