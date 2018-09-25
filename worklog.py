import csv
import datetime
import os
import re
import time

from entry import Entry
from utils import clear_screen
from utils import continue_prompt
from utils import validate_positive_int

class Worklog:
    def __init__(self):
        self.file_name = "entries.csv"
        self.csv_header = "date,name,minutes,note"
        try:
            with open(self.file_name) as file:
                reader = csv.DictReader(file)
                self.entries = list(reader)
        except FileNotFoundError:
            with open(self.file_name, "a") as file:
                file.write(f'{self.csv_header}\n')

        try:
            for i in range(len(self.entries)):
                entry = self.entries[i]
                self.entries[i] = Entry(
                        entry["date"],
                        entry["name"],
                        entry["minutes"],
                        entry["note"]
                )
            print(f"Worklog with {len(self.entries)} entries has been loaded.\n")
            print("Starting program...")
            time.sleep(.5)
        except TypeError:
            raise TypeError("Could not read data file."
                          + " Ensure that CSV is properly formatted.")
        except AttributeError:
            print("No existing worklog found.\nNew worklog has been created.\n")
            print("Starting program...")
            time.sleep(.5)
        

    def save_entries(self):
        with open(self.file_name, "w") as file:
            file.write('date,name,minutes,note\n')
            for entry in self.entries:
                writer = csv.writer(file)
                writer.writerow([entry.date, entry.name, entry.minutes, entry.note])    


    def print_entries(self):
        self.print_selected_entries(self.entries)

    def print_selected_entries(self, entries):
        try:
            for entry in entries:
                print(f'{entry}\n')
        except AttributeError:
            print("No entries exist for this worklog...")


    def add_new_entry(self):
        clear_screen()
        new_entry = Entry.create()
        if new_entry is None:
            print("Add new entry cancelled.  Returning to main menu...")
            time.sleep(1)
            return None
        self.entries.append(new_entry)
        with open(self.file_name, "a") as file:
            writer = csv.writer(file)
            writer.writerow([new_entry.date, new_entry.name, new_entry.minutes, new_entry.note])  


    def lookup_entries(self,selection):
        if selection == "M":
            return None
        else:
            clear_screen()
        # Search by Date
        if selection == "D":
            # Using set comprehension to eliminate duplicates,
            #   but converting to list for sorting
            dates = list({entry.date for entry in self.entries})
            dates.sort()
            print("Select a date the view all entries on that date...")
            for i in range(len(dates)):
                print(f'[{i}] {dates[i]}')
            print("[B] <--BACK---")
            while True:
                try:
                    selection = input(">>> ")
                    if selection.upper() == "B":
                        break
                    selection = int(selection)
                except ValueError:
                    print("Invalid input.  Please choose from the menu.")
                else:
                    clear_screen()
                    selected_date = dates[selection]
                    print(f"*** All tasks for {selected_date} ***\n")
                    for entry in self.entries:
                        if entry.date == selected_date:
                            print(f'{entry}\n')
                    break
        # Search by Time
        elif selection == "T":
            while True:
                try:
                    print("Enter duration (minutes) to search for")
                    searched_minutes = input(">>> ")
                    validate_positive_int(searched_minutes)
                except ValueError as e:
                    print(e)
                else:
                    clear_screen()
                    print(f"*** All tasks with duration {searched_minutes} MINUTES ***\n")
                    results = [entry for entry in self.entries if entry.minutes == searched_minutes]
                    if len(results) > 0:
                        for result in results:
                            print(f"{result}\n")
                    else:
                        print("No entries with that duration found.\n")
                    break
        # Search by String
        elif selection == "S":
            print("Enter a search string.\n")
            print("- NAME and NOTE will be searched for all tasks -")
            print("- Searching IS case-sensitive, but partial matches will be returned -\n")
            search_string = input(">>> ")
            results = [entry for entry in self.entries 
                       if re.search(search_string, entry.name)
                       or re.search(search_string, entry.note)]
            clear_screen()
            print(f"Found {len(results)} matches for string \"{search_string}\"...\n")
            self.print_selected_entries(results)
        # Search by Regex
        else:
            # TODO: Implement search by REGEX
            print("Enter a regular expression (REGEX) to search NAMES and NOTES...")
            input(">>> ")
            pass

        # No matter the path, prompt to hit ENTER for main menu return
        continue_prompt()



    # def clear_entries(self):
    #     clear_screen()
    #     warning_message = '!!! This operation will delete ALL worklog entries.  It is not reversible. !!!'
    #     print('!' * len(warning_message))
    #     print('!!!' + ' ' * (len(warning_message)-6) + '!!!')
    #     print(warning_message)
    #     print('!!!' + ' ' * (len(warning_message)-6) + '!!!')
    #     print('!' * len(warning_message) + '\n')
    #     print('To confirm deletion, type "DELETE" and press ENTER')
    #     confirm_delete = input('>>> ').upper()

    #     if confirm_delete == "DELETE":
    #         with open("entries.csv", "w") as file:
    #             file.write("date,name,minutes,note")
    #         print("\nAll entries have been removed.")
    #     else:
    #         print("\nOPERATION CANCELLED")
    #     print("Returning to main menu...")
    #     time.sleep(1.5)