from menu import Menu

main_menu = Menu({
        "N": "Add New Entry",
        "L": "Lookup Previous Entries",
        "Q": "[QUIT]"
})
    
lookup_menu = Menu({
        "D": "Date",
        "T": "Time Spent",
        "S": "Exact Search",
        "P": "Pattern Search",
        "B": "BACK [main menu]"
})

print(main_menu)