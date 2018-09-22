import datetime
import re

from utils import validate_date_format
from utils import validate_positive_int

class Entry:
    def __init__(self, date, name, minutes, note):
        validate_date_format(date)
        validate_positive_int(minutes)
        
        self.date = date
        self.name = str(name)
        self.minutes = minutes
        self.note = str(note)

    def __str__(self):
        return f'{self.date},{self.name},{self.minutes},{self.note}'

    @classmethod
    def create(cls):
        date = str(input(f"Enter date in YYYY-MM-DD format\n"
                    + "(or press ENTER for {datetime.date.today()})\n>>> ")
                    or datetime.date.today())
        while True:
            try:
                validate_date_format(date)
            except ValueError:
                date = str(input("Couldn't parse entry.  Please try again.\n>>> ")
                    or datetime.date.today())
            else:
                break
        
        name = input("\nEnter task name\n>>> ")
        
        minutes = input("\nEnter number of minutes\n>>> ")
        while True:
            try:
                validate_positive_int(minutes)
            except ValueError as error:
                print(error)
                minutes = input(">>> ")
            else:
                break
        note = input("\nEnter a note for this entry (optional)\n>>> ")
        return cls(date, name, minutes, note)