from messages import *
from utl_funcs import *
from generator import *
import time as ti
from password_database import Password

welcome_message()
relaunch = 1

while relaunch:
    display_menu()
    choice = get_userchoice()
    
    if choice == '1':
        password = pass_generator()
        at_time = ti.time()
        pass_obj = Password(password, at_time)
        print('Your Password is : ', pass_obj.get_password())
    
    elif choice == '2':
        Password.display_all_pass()
    
    elif choice == '3':
        last_past = Password.get_last_password()
        print("Last Password : ", last_past)
    
    elif choice == '4':
        no_of_pass = Password.get_no_of_password()
        print("Total Number of Passwords generated : ", no_of_pass)
    
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
