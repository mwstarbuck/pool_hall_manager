import json
from table import Table
from formatter import Formatter
formatter = Formatter()

# class handles generation of json files for susbsequent billing and for data recovery


class ActivityLog():
    def __init__(self, date):
        self.date = date
        self.entry_list = []
        self.recovery_list = []

    # cretes a play session entry for later billing

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

    # creates a data recocvery entry a checkout for possible app failure. dates left in datetime obj format

    def create_recovery_entry(self, table, start, end):
        rec_entry = {"Table Number": table,
                     "Start Time": str(start), "End Time": str(end)}
        self.recovery_list.append(rec_entry)
        return self.recovery_list

    # writes to json file for billing

    def log_entry(self, entry):
        with open(f'{self.date}.json', 'w') as file_object:
            json.dump(entry, file_object, indent=2)

    # writes to json recovery file

    def rec_entry(self, entry):
        with open(f'{self.date}-rec.json', 'w') as file_object:
            json.dump(entry, file_object, indent=2)

    # loads json recovery file -- json obj conversion

    def recovery(self, date):
        with open(f'{self.date}-rec.json') as file_object:
            recovery_list = json.load(file_object)
        return recovery_list
