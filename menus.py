from menu import Menu

main_menu = Menu({
        "A": "ADD New Entry",
        "E": "EDIT Existing Entry",
        "D": "DELETE Single Entry",
        "C": "CLEAR Entire Worklog",
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
