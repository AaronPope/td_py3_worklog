from menu import Menu

main_menu = Menu({
        "1": "Add New Entry",
        "2": "Lookup Previous Entries"
})
    
lookup_menu = Menu({
        "1": "Date",
        "2": "Time Spent",
        "3": "Exact Search",
        "4": "Pattern Search"
})

print(main_menu)