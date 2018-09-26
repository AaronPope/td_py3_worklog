# Aaron Pope
# 05/22/2018, add more functions 9/20/2018
# Treehouse TechDegree - Python, Unit 3: Work Log

"""An ever-growing mash-up of small utilities"""

import os
import re

EXIT_ARGS = {"Q", "QUIT"}
# Pretty "good enough" for matching dates
DATE_REGEX = re.compile(r'\d{4}-[0-1]?[0-9]-[0-3]?[0-9]')

def exit_check(choice):
    """Close the program if EXIT_ARGS string is passed as argument."""
    if choice in EXIT_ARGS:
        exit()

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def continue_prompt(message="\nPress ENTER to return to main menu..."):
    """Pause the terminal with an input() command.

    This is probably a somewhat hack-ish way to accomplish a pause.
    But passing a string argument for customization rationalizes it...
    """
    input(message)

def validate_date_format(date):
    """Determine if the passed date is valid for format YYYY-MM-DD"""
    if not DATE_REGEX.fullmatch(date):
        raise ValueError(f"Date format could not be parsed. --> {date}\n"
                         + "The required format is \"YYYY-MM-DD\"")

def validate_positive_int(number):
    """Determine if the passed number is a positive integer"""
    try:
        number = int(number)
    except ValueError:
        raise ValueError("Entry must be an integer.")
    else:
        if number < 0:
            raise ValueError("Entry must be a positive number.")
