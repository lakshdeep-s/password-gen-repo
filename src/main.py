from messages import *
from utl_funcs import *
from generator import *

welcome_message()
relaunch = 1

while relaunch:
    display_menu()
    choice = get_userchoice()
    
    if choice == '1':
        password = pass_generator()
        print('Your Password is : ', password)
        
    elif choice.upper() == 'Q':
        break
    
    relaunch_prompt()
    choice = get_userchoice()
    if choice.upper() == 'N':
        relaunch = 0
    elif choice.upper() != "Y":
        print("Unrecognized Entry! exiting...")
        break
exit_message()
