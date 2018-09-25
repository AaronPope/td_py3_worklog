# Aaron Pope
# 09/01/2018
# Treehouse TechDegree - Python, Unit 3: Work Log

from menu import Menu

main_menu = Menu({
        "A": "ADD New Entry",
        "L": "LOOKUP Previous Entries",
        "Q": "---QUIT---"
})
    
lookup_menu = Menu({
        "D": "Date",
        "T": "Time Spent (minutes)",
        "S": "Exact Search (text)",
        "P": "Pattern Search",
        "M": "<--MAIN MENU---"
})
