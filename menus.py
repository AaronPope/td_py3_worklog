from menu import Menu

main_menu = Menu({
        "N": "Add New Entry",
        "L": "Lookup Previous Entries",
        "Q": "Quit"
})
    
lookup_menu = Menu({
        "D": "Date",
        "T": "Time Spent",
        "S": "Exact Search",
        "P": "Pattern Search",
        "B": "Back"
})

print(main_menu)