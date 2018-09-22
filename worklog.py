import csv
import datetime
import os
import time

from entry import Entry
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

        try:
            for i in range(len(self.entries)):
                entry = self.entries[i]
                self.entries[i] = Entry(
                        entry["date"],
                        entry["name"],
                        entry["minutes"],
                        entry["note"]
                )
        except TypeError:
            raise TypeError("Could not read data file."
                          + " Ensure that CSV is properly formatted.")
        

    def print_entries(self):
        try:
            for entry in self.entries:
                print(f'{entry}\n')
        except AttributeError:
            print("No entries exist for this worklog...")


    def add_new_entry(self):
        clear_screen()
        entry = Entry.create()
        with open(self.file_name, "a") as file:
            writer = csv.writer(file)
            writer.writerow([entry.date, entry.name, entry.minutes, entry.note])


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


    def lookup_entries(self,selection):
        if selection == "M":
            return None
        else:
            clear_screen()
        
        if selection == "D":
            # TODO: Implement search by DATE
            input("TODO: Implement search by DATE...")
            pass
        elif selection == "T":
            # TODO: Implement search by TIME
            input("TODO: Implement search by TIME...")
            pass
        elif selection == "S":
            # TODO: Implement search by STRING
            input("TODO: Implement search by STRING...")
            pass
        else:
            # TODO: Implement search by REGEX
            input("TODO: Implement search by REGEX")
            pass
        