import json
import click
import datetime
from jiracmd import cli


@click.group(name="worklog")
def worklog_cli():
    pass

@click.command(name="add")
@click.option('-i', '--issue', required=True)
@click.option('-d', '--date', type=click.DateTime(formats=["%Y-%m-%d"]), default=str(datetime.date.today()))
@click.option('-s', '--start', type=click.DateTime(formats=["%H:%M"]))
@click.option('-e', '--end', type=click.DateTime(formats=["%H:%M"]))
@click.option('-t', '--time-spent')
def worklog_add(issue, date, start, end, time_spent):
    date_str = str(date.date())
    start_str = str(start.time())
    end_str = str(end.time())
    time_diff = end - start
    start_date = datetime.datetime.combine(date.date(), start.time())
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    spent_time = f"{hours}h {minutes}m"
    click.echo(f'== Worklog: add {issue} on {start_date}, spent {spent_time}')
    #response = jira_client.add_worklog(issue, started=start_date, timeSpent=spent_time)


@click.command(name="get")
@click.option('-i', '--issue', required=True)
def worklog_get(issue):
    click.echo(':: Worklog List')
    response = cli.jira._get(f'issue/{issue}/worklog')
    print(json.dumps(response.json(), indent=2))



worklog_cli.add_command(worklog_add)
worklog_cli.add_command(worklog_get)
