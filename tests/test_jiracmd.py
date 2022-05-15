import os
from click.testing import CliRunner
from jiracmd.cli import cli

def test_version_flag():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0

def test_version_output():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--version"])
        assert result.output.startswith("cli, version ")


