from collections import deque

class Password:
    database = deque()
    no_of_passwords = 0
    def __init__(self, password: str, time: str) -> None:
        self.password = password
        self.time_of_gen = time
        self.database.append((time, password))
        Password.no_of_passwords+=1
        
    def get_password(self):
        return self.password
        
    @classmethod
    def get_no_of_password(cls):
        return cls.no_of_passwords
        
    @classmethod
    def get_last_password(cls):
        if cls.database:
            return cls.database[-1][1]
        else:
            return None
        
    @classmethod
    def display_all_pass(cls):
        for time, password in cls.database:
            print("Password:", password, "Time:", time)
            
    