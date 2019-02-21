import json


class ActivityLog():
    def __init__(self, date):
        self.date = date

    def create_entry(self, table, start, end, total_time):
        entry = {
            "Table Number": table, "Start Time": str(start),
            "End Time": str(end), "Total Time Played": str(total_time)
        }
        return entry

    def log_entry(self, entry):
        with open(f'{self.date}.json', 'a') as file_object:
            json.dump(entry, file_object, indent=2)
