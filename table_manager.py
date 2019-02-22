from formatter import Formatter
from table import Table
from datetime import datetime
from time import time
from activity_log import ActivityLog
day = datetime.now()


class TableManager():
    def __init__(self, day):
        self.day = day
        self.date = formatter.date_only(day)
        #self.date = f"{self.day.month}-{self.day.day}-{self.day.year}"

    def print_lines(self):
        print("")
        print("-----------------------------------")
        print("")

    def show_menu(self):
            # show_menu
        print("")
        print(f"-------U of H Pool Hall--------")
        print(f" \t   {self.date}\n")
        print("CHECKOUT TABLE: Enter 1: ")
        print("CHECKIN TABLE: Enter 2: ")
        print("VIEW ALL TABLES: enter 3: ")
        print("To QUIT the app, enter 'q': ")
        self.print_lines()

    def create_tables(self):
        pass

    def show_tables(self):
        current_time = datetime.now()
        print("")
        print("-------U of H Pool Hall-------\n")
        print("         TABLE LIST")
        self.print_lines()
        for table in tables:
            if table.occupied == True:
                status = "Occupied"
            else:
                status = "Available"
             #pretty_date = table.date_formating(table.start_time)
            if table.start_time != "":
                pretty_clock = formatter.clock_format(table.start_time,)
                elapsed_time = formatter.timer_format(
                    current_time, table.start_time)
                print(
                    f"Table-{table.number} - {status} -  Start: {pretty_clock} - Play time: {elapsed_time}")
            else:
                print(
                    f"Table-{table.number} - {status}")
        self.print_lines()

    def choose_table(self, user_input):
        while True:
            try:
                if user_input == "1":
                    choice = int(input("Enter table number to CHECKOUT: ")) - 1

                else:
                    choice = int(input("Enter table number to CHECKIN: ")) - 1
                # for i in range(0, len(tables)):
                #     table = tables[i]
                #     if i == choice:
                table = tables[choice]
                return table
                # table.checkout()
                # self.show_tables()
            except ValueError:
                print("\n")
                print(
                    "*** Please enter a valid table number ***\n\n\nPress RETURN to continue:")
                print("\n")
            except:
                print(
                    "*** Did you spill coffee on you me? ***\n\n\nPress RETURN to continue: ")

    def chooser(self, user_input):
        if user_input == "1":
            self.show_tables()
            table = self.choose_table(user_input)
            table.checkout()
            self.show_tables()
            print(
                f"Table {table.number} has been checked out at: {formatter.clock_format(table.start_time)}")
        elif user_input == "2":
            self.show_tables()
            # check for all availability
            all_available = True
            for table in tables:
                if table.occupied == True:
                    all_available = False
            if all_available == True:
                input(
                    "*** All Tables are available. Choose another menu option. ***\n\n\nPress RETURN to continue: ")
                # self.show_menu()
                # break
            else:
                table = self.choose_table(user_input)
                table.checkin()
                entry = activity_log.create_entry(
                    table.number, table.start_time, table.end_time, table.time_played)
                activity_log.log_entry(entry)
                table.start_time = ""
            self.show_tables()
        elif user_input == "3":
            self.show_tables()

    # def log_activity(self):
    #     with
################ FOR MAIN ############


formatter = Formatter()
manager = TableManager(day)
activity_log = ActivityLog(manager.date)

tables = []
for i in range(1, 13):
    table = Table(i)
    tables.append(table)
# for table in tables:
    # print(f"Table - {table.name}- {table.occupied}")
    # print(manager.day)

user_input = ""
while user_input != "q":
    manager.show_menu()
    user_input = input("Please enter a choice from the menu: ")
    manager.chooser(user_input)
