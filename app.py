# Aaron Pope
# 09/01/2018
# Treehouse TechDegree - Python, Unit 3: Work Log

import csv
import datetime
import json
import sys

import utils

from menus import lookup_menu
from menus import main_menu
from worklog import Worklog



def add_new_entry():
    task_name = input("Enter task name\n>>> ")
    task_minutes = input("\nEnter number of minutes\n>>> ")
    # TODO: Shorten this line
    task_date = input(f"\nEnter date in YYYY-MM-DD format\n(or press ENTER for {datetime.date.today()})\n>>> ") or datetime.date.today()
    task_note = input("\nEnter a note for this entry (optional)\n>>> ")
    # TODO: Remove this
    input(f"{task_name}, {task_minutes}, {task_date}, {task_note}")
    pass

def lookup_entries():
    selection = lookup_menu.get_menu_selection("Lookup by...\n")
    if selection == "B":
        return None
    else:
        utils.clear_screen()
    
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
        

if __name__ == '__main__':
    utils.clear_screen()

    worklog = Worklog()
    worklog.print_entries()
    input("WAIT...")

    while True:
        selection = main_menu.get_menu_selection("What would you like to do?\n") 
        utils.exit_check(selection)

        if selection == "A":
            add_new_entry()
        else:
            lookup_entries()


# N) New Entry
#   - Enter task Name
#   - Enter # of minutes spent working
#   - Enter additional notes
#   ## Return to Main Menu

# L) Lookup Previous Entries
#   D) Find by Date
#   T) Find by Time Spent (number of minutes)
#   S) Find by Search (exact) (in Name or Notes)
#   P) Find by Pattern
#   B) Go Back || M) Main Menu

# Q) Quit
