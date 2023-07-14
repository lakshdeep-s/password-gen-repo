def get_userchoice():
    choice = input("Enter you choice : ")
    return choice

def validate_pass_len(len):
    if len < 8 or len > 14:
        return -1
    return 1