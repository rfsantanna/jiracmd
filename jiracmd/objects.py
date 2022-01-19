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
    created: datetime
    updated: datetime
    started: datetime

    def __post__init(self):
        pass

    def __repr__(self):
        return f"Worklog(id={self.id}, timeSpent={self.timeSpent}, started={self.started})"
        
