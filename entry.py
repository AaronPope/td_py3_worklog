# Aaron Pope
# 09/01/2018
# Treehouse TechDegree - Python, Unit 3: Work Log


import datetime
import re

from utils import validate_date_format
from utils import validate_positive_int

class Entry:
    """An object-oriented representation of a Work Log entry"""
    def __init__(self, date, name, minutes, note):
        """Initialize a new instance of Entry

        date: calendar date on which work was performed
        name: name/title of work log entry
        minutes: time spent on work (expects integer)
        note: extra information about the work log entry
        """
        validate_date_format(date)
        validate_positive_int(minutes)
        
        self.date = date
        self.name = str(name)
        self.minutes = minutes
        self.note = str(note)

    def __str__(self):
        return (f'--- {self.date} ---\nTASK: {self.name}\n'
                + f'DURATION: {self.minutes} minutes\n'
                + f'NOTE: {self.note}')
    

    @classmethod
    def create(cls):
        """Return a new instance of Entry, based on user input """
        cancel_kw = "CANCEL"
        print("*** New Worklog Entry ***")
        print(f"[Type {cancel_kw} (case-sensitve) "
              + "for any field to cancel new entry.]\n")

        # Get user input for Date
        date = str(input(f"Enter date in YYYY-MM-DD format\n"
                    + "(or press ENTER for {datetime.date.today()})\n>>> ")
                    or datetime.date.today())
        if date == cancel_kw:
            return None
        while True:
            try:
                validate_date_format(date)
            except ValueError:
                date = str(input("Couldn't parse entry.  "
                                 + "Please try again.\n>>> ")
                    or datetime.date.today())
            else:
                break
        
        # Get user input for task Name
        name = input("\nEnter task name\n>>> ")
        if name == cancel_kw:
            return None
        
        # Get user input for task Minutes
        minutes = input("\nEnter number of minutes\n>>> ")
        if minutes == cancel_kw:
            return None
        while True:
            try:
                validate_positive_int(minutes)
            except ValueError as error:
                print(error)
                minutes = input(">>> ")
            else:
                break
                
        # Get user input for task Note
        note = input("\nEnter a note for this entry (optional)\n>>> ")
        if note == cancel_kw:
            return None
        
        return cls(date, name, minutes, note)
