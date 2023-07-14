import random
def get_userchoice():
    choice = input()
    return choice

def validate_pass_len(len):
    if len < 8 or len > 14:
        return -1
    return 1

def random_case(string):
    result = ""
    for char in string:
        if char.isalpha():
            if random.choice([True, False]):
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    return result