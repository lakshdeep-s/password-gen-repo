from collections import deque

class Password:
    database = deque()
    def __init__(self, password: str, time: str) -> None:
        self.password = password
        self.time_of_gen = time
        self.database.append((time, password))    
    @classmethod
    def get_last_password(cls):
        if cls.database:
            return cls.database[-1][1]
        else:
            return None
        
    @classmethod
    def display_all_pass(cls):
        times = list(cls.database.keys())
        for time in times:
            print("Password : ", cls.database[time], " Time : ", time)
            
    