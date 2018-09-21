import datetime

class Task:
    def __init__(self, name, date, time_spent, note):
        self.name = str(name)
        try:
            # TODO: Check to see if date is passed in correct format
            pass
        except Exception:
            pass
        try:
            # TODO: Check to see that time_spent is in minutes
            pass
        except Exception:
            pass
        self.time_spent = time_spent
        self.note = str(note)