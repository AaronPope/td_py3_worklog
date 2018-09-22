# Aaron Pope
# 05/22/2018
# Treehouse TechDegree - Python, Unit 2: Secret Messages

import os
import re

EXIT_ARGS = {"Q", "QUIT"}
# Pretty "good enough" for matching dates
date_regex = re.compile(r'\d{4}-[0-1]?[0-9]-[0-3]?[0-9]')

def exit_check(choice):
    if choice in EXIT_ARGS:
        exit()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def validate_date_format(date):
    if not date_regex.fullmatch(date):
        raise ValueError(f"Date format could not be parsed. --> {date}\n"
                         + "The required format is \"YYYY-MM-DD\"")

def validate_positive_int(number):
    try:
        number = int(number)
        pass
    except ValueError:
        raise ValueError("Entry must be an integer.")
    else:
        if number < 0:
            raise ValueError("Entry must be a positive number.")
