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
        date_started = self._to_datetime(self.started, return_string=True)
        return f"Worklog(id={self.id}, timeSpent={self.timeSpent}, started={started})"

    def _to_datetime(self, date_string, return_string=False):
        date_obj = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.000%z')
        if return_string:
            return date_obj.strftime('%Y-%m-%d %H:%M')
        return date_obj

    def _table_dict(self):
        table_dict = {
            "id": self.id,
            "issueId": self.issueId,
            "started": self._to_datetime(self.started, return_string=True),
            "timeSpent": self.timeSpent
        }
        return table_dict
