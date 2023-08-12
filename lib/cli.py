import re
import time
from prettycli import red
from simple_term_menu import TerminalMenu
from models import Owner


class Cli():
    
    def __init__(self):
        current_owner = None
        
    def start(self):
        self.clear_screen(44)
        options = ["Login", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        if options[menu_entry_index] == "Login":
            self.handle_login()
        else:
            self.exit()
            
    def clear_screen(self, lines):
        print("\n" * lines)
        
    def handle_login(self):
        email = input("Please enter your email:\n\n")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, email):
            print("Find a user by email")
            owner = Owner.find_or_create_by(email)
            
            self.current_owner = owner
            
            print(f"Hello, {owner.email} 👋")
            
            self.show_owner_options()
            
        else:
            print(red("Invalid email. Please try again!"))
            time.sleep(2)
            self.start()
        
    def show_owner_options(self):
        options = ["My Toys", "New Toy", "Edit My Info", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        print(options[menu_entry_index])
        
    
    def exit(self):
        print("Bye!")
    
    
app = Cli()
app.start()

# def start():
#         options = ["My toys", "Add toy", "Exit"]
#         terminal_menu = TerminalMenu(options)
#         menu_entry_index = terminal_menu.show()
#         print(f"You have selected {options[menu_entry_index]}!")
#     # print("Welcome to Toy Tracker!\n")
#     # print("1. My Toys")
#     # print("2. Add Toy")
#     # print("3. Exit")
#     # user_input = input("Please make a selection (1-3)")
    
#     # handle_user_input(user_input) # Retun a value that sends the user back to beginning
    
    
# def handle_user_input(input):
#     is_number = input.isdigit()
#     if is_number:
#         selection = int(input)
#         if 1 <= selection <= 3:
#             handle_selection(selection)
#     else:
#         print(red("incorrect selection"))
#         start()
        
        
#     # is this input an integer and is it 1 - 3
    
    
    
# start()