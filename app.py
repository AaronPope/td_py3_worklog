# Aaron Pope
# 09/01/2018
# Treehouse TechDegree - Python, Unit 3: Work Log

""" Serves as the launch point for the Work Log tool """

from menus import lookup_menu
from menus import main_menu
from utils import clear_screen
from utils import continue_prompt
from utils import exit_check
from worklog import Worklog        

if __name__ == '__main__':
    clear_screen()

    worklog = Worklog()

    while True:
        selection = main_menu.get_menu_selection("What would you like to do?\n") 
        exit_check(selection)

        if selection == "A":
            worklog.add_new_entry()
        elif len(worklog.entries) == 0:
                clear_screen()
                print("This worklog does not yet contain any entries.")
                print("Please go add some before searching!")
                continue_prompt()
        else:
            worklog.lookup_entries(lookup_menu.get_menu_selection("Lookup by...\n"))
