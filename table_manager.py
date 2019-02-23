from formatter import Formatter
from table import Table
from datetime import datetime
from time import time
from activity_log import ActivityLog
day = datetime.now()

# table manager control center for all pool hall/app functions


class TableManager():
    def __init__(self, day):
        self.day = day
        self.date = formatter.date_only(day)
        # self.date = f"{self.day.month}-{self.day.day}-{self.day.year}"

    def print_lines(self):
        print("")
        print("-----------------------------------")
        print("")
    # Main app menu

    def show_menu(self):
            # show_menu
        print("")
        print(f"-------U of H Pool Hall--------")
        print(f" \t   {self.date}\n")
        print("CHECKOUT TABLE: Enter 1: ")
        print("CLOSE TABLE: Enter 2: ")
        print("VIEW ALL TABLES: enter 3: ")
        print("DATA RECOVERY: enter 4: ")
        print("To QUIT the app, enter 'q': ")
        self.print_lines()

    # function shows a list of all tables with current status
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
    # function handles main menu choice and returns table choice to chooser() function

    def choose_table(self, user_input):
        while True:
            try:
                if user_input == "1":
                    choice = int(input("Enter table number to CHECKOUT: ")) - 1

                else:
                    choice = int(input("Enter table number to CLOSE: ")) - 1

                table = tables[choice]
                return table
                # table.checkout()
                # self.show_tables()
            except ValueError:
                print("\n")
                print(
                    "*** Please enter a valid table number ***:")
                print("\n")
            except:
                print(
                    "*** Did you spill coffee on you me? ***\n\n\nPress RETURN to continue: ")

    # function to re-assign attributes to table obj. from a json data recovery file
    def repopulate_data(self, json_data):
        recovery_time = datetime.now()
        for i in range(len(json_data)):
            temp_table = json_data[i]
            temp_table_no = int(temp_table["Table Number"])
            print(temp_table_no)
            for table in tables:
                if table.number == temp_table_no:
                    table.occupied = True
                    table.start_time = datetime.strptime(
                        temp_table["Start Time"], "%Y-%m-%d %H:%M:%S.%f")
                    table.end_time = recovery_time

    # method handles all choices from main menu.  -- needs cleaning up
    def chooser(self, user_input):
        if user_input == "1":
            print("")
            confirmation = input(
                "Checkout Table?\nEnter yes or no y/n: ").lower()
            if confirmation == "n":
                print("")
            elif confirmation == "y":
                self.show_tables()
                table = self.choose_table(user_input)
                table.checkout()
                recovery_list = activity_log.create_recovery_entry(
                    table.number, table.start_time, table.end_time)
                activity_log.rec_entry(recovery_list)
                self.show_tables()
                print(
                    f"Table {table.number} has been checked out at: {formatter.clock_format(table.start_time)}")
            else:
                print("")
                print("*** You did not enter a valid response.  Try again champ. ***")

        elif user_input == "2":
            print("")
            confirmation = input(
                "Close out Table?\nEnter yes or no y/n: ").lower()
            if confirmation == "n":
                print("")
            elif confirmation == "y":
                self.show_tables()
                # check for all availability
                all_available = True
                for table in tables:
                    if table.occupied == True:
                        all_available = False
                if all_available == True:
                    print("")
                    input(
                        "*** All Tables are available. Choose another menu option. ***\n\n\nPress RETURN to continue: ")
                    # self.show_menu()
                    # break
                else:
                    table = self.choose_table(user_input)
                    status = table.checkin()
                    if status == True:
                        entry = activity_log.create_entry(
                            table.number, table.start_time, table.end_time, table.time_played)
                        activity_log.log_entry(entry)
                        table.start_time = ""
                        self.show_tables()
                        print(
                            f"Table {table.number} has been closed out at: {formatter.clock_format(table.end_time)}")

            else:
                print("")
                print("*** You did not enter a valid response.  Try again champ. ***")

        elif user_input == "3":
            self.show_tables()

        elif user_input == "4":
            print("")
            confirmation = input(
                "Recover table activity?\nEnter yes or no y/n: ").lower()
            if confirmation == "n":
                print("")
            elif confirmation == "y":
                recovery_list = activity_log.recovery(self.date)
                self.repopulate_data(recovery_list)
                self.show_tables()
            else:
                print("")
                print("*** You did not enter a valid response.  Try again champ. ***")

################ running of the app below ############


# creating instances of  classes to run app
formatter = Formatter()
manager = TableManager(day)
activity_log = ActivityLog(manager.date)

# creating list and filling  it with table objects
tables = []
for i in range(1, 13):
    table = Table(i)
    tables.append(table)
# for table in tables:
    # print(f"Table - {table.name}- {table.occupied}")
    # print(manager.day)

# while loop that keeps app in a running state until user quits with 'q'
user_input = ""
while user_input != "q":
    manager.show_menu()
    user_input = input("Please enter a choice from the menu: ")
    manager.chooser(user_input)
