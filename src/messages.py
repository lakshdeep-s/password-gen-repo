#Main Generator Message 
def welcome_message():
    print("-------------------------------------\nWelcome ! To Password Generator..")
    print("-------------------------------------")
    
def display_menu():
    print("\n-------\n'1' For Creating a Password.")
    print("'q' For Exiting app.")
    print("Under Development....\n------------")
    print("What would you like to do ? : ", end="")

def relaunch_prompt():
    print("\nWould you like to go again (Y/N) ? : ", end="")

def exit_message():
    print("-------\nProgram Ended, Visit Again !\n-------")
    
def password_len_prompt():
    print("\nEnter the Password Length (atleast 8) : ",end="")

def len_error_message():
    print("-------\nPassword length not within range(8,14).\n-------")