# Aaron Pope
# 09/01/2018
# Treehouse TechDegree - Python, Unit 3: Work Log

import csv
import datetime
import sys

import utils
from menus import lookup_menu
from menus import main_menu



def add_new_entry():
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

    with open("entries.csv") as file:
        reader = csv.DictReader(file)
        all_tasks = list(reader)

    while True:
        selection = main_menu.get_menu_selection("What would you like to do?\n") 
        utils.exit_check(selection)

        if selection == "A":
            add_new_entry()
        else:
            lookup_entries()

    for task in all_tasks:
        print(task)


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
