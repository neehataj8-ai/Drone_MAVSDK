from datetime import datetime

class Logger:

    def log(self, message):

        with open("logs/events.txt","a") as file:

            file.write(
                f"{datetime.now()} : {message}\n"
            )