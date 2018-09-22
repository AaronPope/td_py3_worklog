# Aaron Pope
# 09/01/2018
# Treehouse TechDegree - Python, Unit 3: Work Log

import utils

from menus import lookup_menu
from menus import main_menu
from worklog import Worklog
from entry import Entry
        

if __name__ == '__main__':
    utils.clear_screen()

    worklog = Worklog()

    while True:
        selection = main_menu.get_menu_selection("What would you like to do?\n") 
        utils.exit_check(selection)

        if selection == "A":
            worklog.add_new_entry()
        elif selection == "C":
            worklog.clear_entries()
        else:
            worklog.lookup_entries(lookup_menu.get_menu_selection("Lookup by...\n"))
