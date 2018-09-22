import csv
import datetime
import os
import time

from entry import Entry
from utils import clear_screen

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
            time.sleep(1.5)
        except TypeError:
            raise TypeError("Could not read data file."
                          + " Ensure that CSV is properly formatted.")
        except AttributeError:
            print("No existing worklog found.\nNew worklog has been created.\n")
            print("Starting program...")
            time.sleep(1.5)
        

    def save_entries(self):
        with open(self.file_name, "w") as file:
            file.write('date,name,minutes,note\n')
            for entry in self.entries:
                writer = csv.writer(file)
                writer.writerow([entry.date, entry.name, entry.minutes, entry.note])    


    def print_entries(self):
        try:
            for entry in self.entries:
                print(f'{entry}\n')
        except AttributeError:
            print("No entries exist for this worklog...")


    def add_new_entry(self):
        clear_screen()
        self.entries.append(Entry.create())
        new_entry = self.entries[-1]
        with open(self.file_name, "a") as file:
            writer = csv.writer(file)
            writer.writerow([new_entry.date, new_entry.name, new_entry.minutes, new_entry.note])  
            


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


    def lookup_entries(self,selection):
        if selection == "M":
            return None
        else:
            clear_screen()
        
        if selection == "D":
            # TODO: Implement search by DATE
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
                    for entry in self.entries:
                        if entry.date == selected_date:
                            print(f'{entry}\n')
                    break
            input("\nPress ENTER to return to main menu...")

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
        