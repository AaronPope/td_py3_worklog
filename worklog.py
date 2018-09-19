# Aaron Pope
# 09/01/2018
# Treehouse TechDegree - Python, Unit 3: Work Log

import csv
import datetime

import utils
import menus


if __name__ == '__main__':
    utils.clear_screen()

    with open("entries.csv") as file:
        reader = csv.DictReader(file)
        all_tasks = list(reader)

    while True:
        menus.main_menu.get_menu_selection("What would you like to do?\n")
        menus.lookup_menu.get_menu_selection("Lookup by...\n")

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
