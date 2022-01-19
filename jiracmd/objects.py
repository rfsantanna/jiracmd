import json
from dataclasses import dataclass
from datetime import datetime

 
@dataclass
class Worklog:
    id: str
    self: str
    author: dict
    updateAuthor: dict
    timeSpent: str 
    timeSpentSeconds: int
    issueId: str
    created: str
    updated: str
    started: str

    def __repr__(self):
        date_started = datetime.strptime(self.started, '%Y-%m-%dT%H:%M:%S.000%z')
        started = date_started.strftime('%Y-%m-%d %H:%M')
        return f"Worklog(id={self.id}, timeSpent={self.timeSpent}, started={started})"

