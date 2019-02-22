import json
from table import Table
from formatter import Formatter
formatter = Formatter()


class ActivityLog():
    def __init__(self, date):
        self.date = date
        self.entry_list = []

    def create_entry(self, table, start, end, total_time):
        f_start = formatter.date_format(start)
        f_end = formatter.date_format(end)
        f_total_time = formatter.timer_format(end, start)
        cost = formatter.cost_calc(end, start)
        entry = {
            "Table Number": table, "Start Time": f_start,
            "End Time": f_end, "Total Time Played": f_total_time, "Cost": cost
        }
        self.entry_list.append(entry)
        return self.entry_list

    def log_entry(self, entry):
        with open(f'{self.date}.json', 'w') as file_object:
            json.dump(entry, file_object, indent=2)
