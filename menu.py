# Aaron Pope
# 09/01/2018
# Treehouse TechDegree - Python, Unit 3: Work Log

from utils import clear_screen

class Menu:
    """An object to create and manipulate terminal menus"""
    def __init__(self, options):
        """Create a new instance of Menu
        
        options: dictionary with format {"selection key": "menu item text"}
                 for each element
        """
        self.options = options

    def print_options(self, clear = False):
        """Print each Menu option key/value pair to the terminal"""
        if clear:
            clear_screen()
        for key, value in self.options.items():
            print(f"[{key}] {value}")
    
    def prompt_with_options(self, clear = False):
        """Print Menu options to terminal & return a selection"""
        self.print_options(clear)
        return input(">>> ").upper()

    def get_menu_selection(self, direction_text="Make a selection...", clear=True):
        """Return a valid selection from options.keys()"""
        if clear:
            clear_screen()
        print(direction_text)
        selection = self.prompt_with_options()
        if selection in self.options.keys():
            return selection
        
        while selection not in self.options.keys():
            clear_screen()
            print("INVALID ENTRY.  "
                  + "M)Make a selection from the available options...\n")
            print(direction_text)
            selection = self.prompt_with_options()
        return selection
            