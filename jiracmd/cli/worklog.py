import json
import click
import datetime
from pprint import pprint
from jiracmd import cli
from jiracmd.objects import Worklog


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
    body = json.dumps({
        "started": start_date.astimezone().strftime('%Y-%m-%dT%H:%M:%S.000%z'),
        "timeSpent": spent_time
    })
    print(body)
    response = cli.jira._post(f'issue/{issue}/worklog?adjustEstimate=auto', body)
    click.echo(json.dumps(response.json()))


@click.command(name="get")
@click.option('-i', '--issue', required=True)
def worklog_get(issue):
    click.echo(':: Worklog List')
    response = cli.jira._get(f'issue/{issue}/worklog')
    worklogs = [Worklog(**w) for w in response.json()['worklogs']]
    pprint(worklogs)

worklog_cli.add_command(worklog_add)
worklog_cli.add_command(worklog_get)
