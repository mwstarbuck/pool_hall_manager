from datetime import datetime
time = datetime.now()


class Table:
    def __init__(self, number):
        self.number = number
        self.occupied = False
        self.start_time = ""
        self.end_time = ""
        self.time_played = ""
        self.current_time = ""

    # def date_formating(self, time):
    #     pretty_time = f"{time.hour}:{time.minute}"
    #     return pretty_time
    def timer_format(self, end, start):
        delta_time = end - start
        delta_sec = delta_time.total_seconds()
        hours = round(delta_sec / (60 * 60))
        rem_minutes = delta_sec % (60 * 60)
        minutes = round(rem_minutes / 60)
        pretty_timer = f"{hours} hrs : {minutes} min"
        return pretty_timer

    def clock_format(self, time):
        hour = time.hour
        minute = time.minute
        if minute < 10:
            minute = f"0{minute}"
            clock = "AM"
        if hour > 12:
            hour -= 12
            clock = "PM"
        pretty_time = f"{hour}:{minute}{clock}"
        return pretty_time

    # def timer_formating(self, time):
    #     hour = time.hour
    #     minute = time.minute
    #     pretty_timer = f"{hour}:{minute}"
    #     return pretty_timer

    def checkout(self):
        if self.occupied == True:
            input(
                f" !!Table {self.number} is currently occupied!! Please choose another. Hit RETURN.")
        else:
            self.occupied = True
            self.start_time = datetime.now()

    def checkin(self):
        if self.occupied == False:
            input(
                " !!This table is currently available!! Please choose another table. Hit RETURN.")
        else:
            self.occupied = False
            self.end_time = datetime.now()
            self.time_played = self.end_time - self.start_time
            # self.start_time = ""
