import csv
import datetime

class Worklog:
    def __init__(self):
        with open("entries.csv") as file:
            reader = csv.DictReader(file)
            self.entries = list(reader)

    def print_entries(self):
        for entry in self.entries:
            print(entry)

    def add_new_entry(self):
        task_name = input("Enter task name\n>>> ")
        task_minutes = input("\nEnter number of minutes\n>>> ")
        # TODO: Shorten this line
        task_date = input(f"\nEnter date in YYYY-MM-DD format\n(or press ENTER for {datetime.date.today()})\n>>> ") or datetime.date.today()
        task_note = input("\nEnter a note for this entry (optional)\n>>> ")
        # TODO: Remove this
        input(f"{task_name}, {task_minutes}, {task_date}, {task_note}")
        pass