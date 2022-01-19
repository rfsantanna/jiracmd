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
def worklog_add(issue, date, start, end):
    date_str = str(date.date())
    start_str = str(start.time())
    end_str = str(end.time())
    time_diff = end - start
    start_date = datetime.datetime.combine(date.date(), start.time())
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    time_spent = f"{hours}h {minutes}m"
    body = json.dumps({
        "started": start_date.astimezone().strftime('%Y-%m-%dT%H:%M:%S.000%z'),
        "timeSpent": time_spent
    })
    response = cli.jira._post(f'issue/{issue}/worklog?adjustEstimate=auto', body)
    click.echo(Worklog(**response.json()))


@click.command(name="list")
@click.option('-i', '--issue', required=True)
def worklog_list(issue):
    response = cli.jira._get(f'issue/{issue}/worklog')
    worklogs = [Worklog(**w) for w in response.json()['worklogs']]
    pprint(worklogs)

@click.command(name="delete")
@click.option('-i', '--issue', required=True)
@click.option('-w', '--worklog-id', required=True)
def worklog_delete(issue, worklog_id):
    response = cli.jira._delete(f'issue/{issue}/worklog/{worklog_id}')
    try:
        response.json()
        click.echo(json.dumps(response.json(), indent=2))
    except ValueError:
        click.echo(response.content)

worklog_cli.add_command(worklog_add)
worklog_cli.add_command(worklog_delete)
worklog_cli.add_command(worklog_list)
