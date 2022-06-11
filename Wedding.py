import csv
from Person import *
from Table import *

class Wedding:
    def __init__(self):
        self.tables = []
        self.unassigned_people = []
        self.max_seats = 0
        self.last_id = 0
    def add_table(self, table):
        self.tables.append(table)
    def add_person(self, person):
        self.unassigned_people.append(person)
    def remove_person(self, person):
        self.unassigned_people.remove(person)
    # asks for max seats per table.
    def query_max_seats(self):
        while True:
            # seats = input("Please enter the maximum number of people per table: ")
            seats = 6#

            try: seats = int(seats)
            except: print("please enter an integer")
            if isinstance(seats, int): return seats

    def start(self):
        while True:
            # start = input("Open up 'input.csv' in the program directory and input the name, age and spouse (if they have one) of all the guests. Please refer to 'input_example.csv' for an example input. Once you entered all the infomation into 'input.csv' type 'start' and press enter: ")
            start = "start"#
            if start == "start": return None
    def open_csv(self):
        csv_file = open('input.csv', 'r')
        csv_reader = csv.reader(csv_file)
        for name, age, spouse in csv_reader:
            # print(name, age, spouse)

            self.add_person(Person(name, age, spouse))
            if name == "NAME": continue

    # Creates tables
    def create_tables(self):
        num_people = len(self.unassigned_people)
        tables = (num_people // self.max_seats) + (num_people % self.max_seats > 0)
        for i in range(tables):
            table = Table(self.max_seats, i)
            self.add_table(table)
            # print(table.id, ":", table.max_seats)