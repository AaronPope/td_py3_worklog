import csv
import datetime
import os
import time

from utils import clear_screen

class Worklog:
    def __init__(self):
        self.file_name = "entries.csv"
        try:
            with open(self.file_name) as file:
                reader = csv.DictReader(file)
                self.entries = list(reader)
        except FileNotFoundError:
            with open(self.file_name, "a") as file:
                file.write("date,name,minutes,note\n")
        

    def print_entries(self):
        try:
            for entry in self.entries:
                print(entry)
        except AttributeError:
            print("No entries exist for this worklog...")


    def add_new_entry(self):
        clear_screen()
        task_name = input("Enter task name\n>>> ")
        task_minutes = input("\nEnter number of minutes\n>>> ")
        # TODO: Shorten this line
        task_date = input(f"\nEnter date in YYYY-MM-DD format\n"
                    + "(or press ENTER for {datetime.date.today()})\n>>> ") or datetime.date.today()
        task_note = input("\nEnter a note for this entry (optional)\n>>> ")
        with open(self.file_name, "a") as file:
            file.write(f"{task_date},{task_name},{task_minutes},{task_note}\n")


    def clear_entries(self):
        clear_screen()
        print("This operation will delete ALL worklog entries.  It is not reversible.")
        print('To continue, type "DELETE" and press ENTER')
        confirm_delete = input(">>> ").upper()

        if confirm_delete == "DELETE":
            with open("entries.csv", "w") as file:
                file.write("")
            print("\nAll entries have been removed.")
        else:
            print("\nOPERATION CANCELLED")
        print("Returning to main menu...")
        time.sleep(1.5)
            