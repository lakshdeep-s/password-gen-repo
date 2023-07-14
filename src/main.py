from messages import *
from utl_funcs import *

welcome_message()
display_menu()
choice = str()

while choice.upper() != 'Q':
    choice = get_userchoice()
    
    if choice == '1':
        pass
    
    if choice.upper() == 'Q':
        exit_message()
        exit(1)
    print("Some Test")