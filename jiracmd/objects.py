import json
from dataclasses import dataclass
from jiracmd.jira import JiraObject

@dataclass
class Worklog(JiraObject):
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

    def _table_dict(self):
        table_dict = {
            "id": self.id,
            "issueId": self.issueId,
            "started": self._to_datetime(
                self.started,
                return_string=True
            ),
            "timeSpent": self.timeSpent
        }
        return table_dict

@dataclass
class Issue(JiraObject):
    id: str
    self: str
    expand: str
    key: str
    fields: dict

    def _table_dict(self):
        table_dict = {
            "Key": self.key,
            "Type": self.fields['issuetype']['name'],
            "Updated": self._to_datetime(
                self.fields['updated'],
                return_string=True
            ),
            "Summary": self.fields['summary']
        }
        return table_dict

