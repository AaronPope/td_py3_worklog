# Aaron Pope
# 09/01/2018
# Treehouse TechDegree - Python, Unit 3: Work Log

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
    """An object to represent a collection of Entries"""
    def __init__(self):
        """Create a new Worklog instance

        Initialization will attempt to load "./entries.csv".
        If the file cannot be found,
            it will be created, and 'self.entries' will be
            initialized as an empty list.
        If the file is found,
            __init__ will attempt to read each line (task)
            and store it as an Entry object in the list 'self.entries'.
        If the file is found but cannot be read,
            'self.entries' will be initilized as an empty list.
        """
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
            self.entries = []
            print("Starting program...")
            time.sleep(.5)
        

    def save_entries(self):
        """Write each Entry in 'self.entries' to './entries.csv'

        This operation overwrites the contents of './entries.csv'
        """
        with open(self.file_name, "w") as file:
            file.write('date,name,minutes,note\n')
            for entry in self.entries:
                writer = csv.writer(file)
                writer.writerow([entry.date, entry.name, entry.minutes, entry.note])    


    def print_entries(self):
        """Print each Entry in 'self.entries'"""
        self.print_selected_entries(self.entries)

    def print_selected_entries(self, entries):
        """Print a subset of 'self.entries'"""
        try:
            for entry in entries:
                print(f'{entry}\n')
        except AttributeError:
            print("No entries exist for this worklog...")


    def add_new_entry(self):
        """Append a new Entry to 'self.entries'"""
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

    
    def regex_entry_search(self, expression):
        """Regex search the 'name' and 'note' attributes for each Entry in 'self.entries

        expression: A regular expression input by the user
        """
        return [entry for entry in self.entries 
                if re.search(expression, entry.name)
                or re.search(expression, entry.note)]


    def search_by_date(self):
        """Prompt for selection of valid date & display associated entries"""
        # Using set comprehension to eliminate duplicates,
        #   but converting to list for sorting
        dates = list({entry.date for entry in self.entries})
        dates.sort()
        print("*** Lookup by Date ***\n")
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


    def search_by_time(self):
        print("*** Lookup by Task Duration ***\n")
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


    def search_by_string(self):
        """Search within 'name' and 'note' for all entries, by string
        
        Prompts the user to input a string.
        The user's input will be used as the search criterion.
        Searching is case-sensitive.
        Partial matches are considered hits.

        This actually re-uses regex search, since a string is just a
            very specific regex match criterion.
        """
        print("*** String Search ***\n")
        print("Enter a search string.\n")
        print("- NAME and NOTE will be searched for all tasks -")
        print("- Searching IS case-sensitive, but partial matches will be returned -\n")
        while True:
            try:
                search_string = input(">>> ")
                results = self.regex_entry_search(search_string)
            except re.error:
                print("Couldn't parse search query.  Please try again.")
            else:
                clear_screen()
                print(f"Found {len(results)} matches for string \"{search_string}\"...\n")
                self.print_selected_entries(results)
                break


    def search_by_regex(self):
        """Search within 'name' and 'note' for all entries, by regex

        Prompts the user to input a regex.
        The user's input will be used as the search criterion.
        """
        print("*** Regex Search ***\n")
        print("Enter a regular expression (REGEX) to search NAMES and NOTES...")
        print("DO NOT include either single (') or double (\") quotes")
        while True:
            try:
                regex = input(">>> ")
                results = self.regex_entry_search(regex)
            except:
                print("Couldn't parse regex.  Please try again")
            else:
                clear_screen()
                print(f"Found {len(results)} matches for regex \"{regex}\"...\n")
                self.print_selected_entries(results)
                break


    def lookup_entries(self, selection):
        """Process the selected lookup operation

        selection: A singler-letter string, corresponding to a menu selection
        """
        if selection == "M":
            return None
        else:
            clear_screen()
            if selection == "D":
                self.search_by_date()
            elif selection == "T":
                self.search_by_time()
            elif selection == "S":
                self.search_by_string()
            else:
                self.search_by_regex()
        # No matter the path, prompt to hit ENTER for main menu return
        continue_prompt()



    def clear_entries(self):
        clear_screen()
        warning_message = '!!! This operation will delete ALL worklog entries.  It is not reversible. !!!'
        print('!' * len(warning_message))
        print('!!!' + ' ' * (len(warning_message)-6) + '!!!')
        print(warning_message)
        print('!!!' + ' ' * (len(warning_message)-6) + '!!!')
        print('!' * len(warning_message) + '\n')
        print('To confirm deletion, type "DELETE" and press ENTER')
        confirm_delete = input('>>> ').upper()

        if confirm_delete == "DELETE":
            with open("entries.csv", "w") as file:
                file.write("date,name,minutes,note")
            print("\nAll entries have been removed.")
        else:
            print("\nOPERATION CANCELLED")
        print("Returning to main menu...")
        time.sleep(1.5)