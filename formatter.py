class Formatter():
    def __init__(self):
        self.clock = ""

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
            self.clock = "AM"
        if hour > 12:
            hour -= 12
            self.clock = "PM"
        pretty_time = f"{hour}:{minute} {self.clock}"
        return pretty_time

    def cost_calc(self, end, start):
        delta_time = end - start
        delta_sec = delta_time.total_seconds()
        hours = round(delta_sec / (60 * 60))
        rem_minutes = delta_sec % (60 * 60)
        minutes = round(rem_minutes / 60)
        cost = f"${(hours * 30.00) + (minutes * 0.50)}0"
        return cost
    # def timer_formating(self, time):
    #     hour = time.hour
    #     minute = time.minute
    #     pretty_timer = f"{hour}:{minute}"
    #     return pretty_timer

    def date_format(self, date_obj):
        pretty_date_time = f"{date_obj.month}-{date_obj.day}-{date_obj.year} {self.clock_format(date_obj)}"
        return pretty_date_time

    def date_only(self, date_obj):
        pretty_date = f"{date_obj.month}-{date_obj.day}-{date_obj.year}"
        return pretty_date
