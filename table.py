from datetime import datetime
time = datetime.now()

# table class


class Table:
    def __init__(self, number):
        self.number = number
        self.occupied = False
        self.start_time = ""
        self.end_time = ""
        self.time_played = ""
        self.current_time = ""

    # function changes attributes for checked out status

    def checkout(self):
        if self.occupied == True:
            print("")
            input(
                f" !!Table {self.number} is currently occupied!! Please choose another. Hit RETURN.")
        else:
            self.occupied = True
            self.start_time = datetime.now()
            self.end_time = datetime.now()
            self.time_played = self.end_time - self.start_time

    # changes attributes to a closed out state and calculates delta time

    def checkin(self):
        if self.occupied == False:
            print("")
            input(
                " !!This table is currently available!! Please choose another table. Hit RETURN.")
            return False
        else:
            self.occupied = False
            self.end_time = datetime.now()
            self.time_played = self.end_time - self.start_time
            # self.start_time = ""
            return True
