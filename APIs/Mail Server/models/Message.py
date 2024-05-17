import json

class Message: 
    def __init__(self, _from, to, subject, date, content):
        self._from = _from
        self.to = to
        self.subject = subject
        self.date = date
        self.content = content
        self.spam = False
        
    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)