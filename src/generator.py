from utl_funcs import *
from messages import len_error_message, password_len_prompt
import random, string

def pass_generator():
    # Empty String used for storing the password
    password = str()
    
    # Prompt to enter the length of the password
    password_len_prompt()
    length = int(get_userchoice())
    
    # Check and Validate User Entered password Length
    can_proceed = validate_pass_len(length)
    
    if can_proceed == 1:
        # Adding (2) Special Characters to the password String
        for i in range(2):
            password+=random.choice(string.punctuation)
            
        # Adding (4) Digits to the password String
        for i in range(4):
            password+=random.choice(string.digits)
            
        # Adding an uppercase letter to the Password String
        password+=random.choice(string.ascii_uppercase)
        
        # Adding rest with lowercase letters
        for i in range(length - 7):
            password+=random.choice(string.ascii_letters)
    
    else :
        # Displays length entered Out of Range / Ends program
        len_error_message()
        exit(1)
    
    # Randomly changes the case of letters in password
    password = random_case(password)
    
    # Shuffles the characters in the password
    password = ''.join(random.sample(password, length))
    
    return password