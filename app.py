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



def lookup_entries():
    selection = lookup_menu.get_menu_selection("Lookup by...\n")
    if selection == "M":
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
            worklog.add_new_entry()
        elif selection == "C":
            worklog.clear_entries()
        else:
            lookup_entries()
