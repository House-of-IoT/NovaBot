
from datetime import date

today = date.today()


class Logger:
    def __init__(self):
        self.succ_count = 0
        self.errors = 0

    def write_to_log_file(message):
        with open("../logs.txt" , "r") as file:
            file.writeline(message)

    def error(self , message):
        today = date.today()
        new_message = str(today) +" error:" + message
        self.write_to_log_file(new_message)

    def start():
        message = "Starting Nova.."
        self.write_to_log_file(message)
    
    
