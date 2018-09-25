# Aaron Pope
# 05/22/2018, add more functions 9/20/2018
# Treehouse TechDegree - Python, Unit 3: Work Log

import os
import re

EXIT_ARGS = {"Q", "QUIT"}
# Pretty "good enough" for matching dates
DATE_REGEX = re.compile(r'\d{4}-[0-1]?[0-9]-[0-3]?[0-9]')

def exit_check(choice):
    if choice in EXIT_ARGS:
        exit()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def continue_prompt():
    input("\nPress ENTER to return to main menu...")

def validate_date_format(date):
    if not DATE_REGEX.fullmatch(date):
        raise ValueError(f"Date format could not be parsed. --> {date}\n"
                         + "The required format is \"YYYY-MM-DD\"")

def validate_positive_int(number):
    try:
        number = int(number)
    except ValueError:
        raise ValueError("Entry must be an integer.")
    else:
        if number < 0:
            raise ValueError("Entry must be a positive number.")
