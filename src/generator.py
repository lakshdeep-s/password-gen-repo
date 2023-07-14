from utl_funcs import *
from messages import len_error_message, password_len_prompt
import random, string

def pass_generator():
    password = str()
    
    password_len_prompt()
    length = int(get_userchoice())
    can_proceed = validate_pass_len(length)
    
    if can_proceed == 1:
        for i in range(2):
            password+=random.choice(string.punctuation)
        for i in range(4):
            password+=random.choice(string.digits)
        #adding an uppercase letter
        password+=random.choice(string.ascii_uppercase)
        #filling rest with lcase letters
        for i in range(length - 7):
            password+=random.choice(string.ascii_letters)
    else :
        len_error_message()
        return ""
    
    password = random_case(password)
    password = ''.join(random.sample(password, length))
    return password

res = pass_generator()
print(res)