from utl_funcs import *
import random, string

def pass_generator():
    password = str()
    
    print("Enter the Password Length (atleast 8) : ",end="")
    len = int(get_userchoice())
    can_proceed = validate_pass_len(len)
    
    if can_proceed:
        for i in range(2):
            password+=random.choice(string.punctuation)
        for i in range(4):
            password+=random.choice(string.digits)
        #adding an uppercase letter
        password+=random.choice(string.ascii_uppercase)
        #filling rest with lcase letters
        for i in range(len - 7):
            password+=random.choice(string.ascii_letters)
    else :
        pass
    
    password = random_case(password)
    
    password = ''.join(random.sample(password, len))
    return password
