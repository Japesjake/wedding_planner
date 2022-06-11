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
        max_seats = self.max_seats
        people = len(self.unassigned_people)
        tables = people // max_seats
        leftover_people = people % max_seats
        full_tables = tables - leftover_people
        not_full_tables = tables - full_tables
        for i in range(full_tables):
            table = Table(max_seats, i)
            print(table.max_people, ":", table.id)
        for i in range(full_tables, not_full_tables + 1):
            table = Table(max_seats - 1, i)
            print(table.max_people, ":", table.id)
    # Creates tables with max seats
    def create_main_tables(self):
        people = len(self.unassigned_people)
        main = people // self.max_seats
        for i in range(main):
            table = Table(self.max_seats, i)
            self.add_table(table)
            self.last_id = i
            print(table.id)
        print("less")

    # Creates tables with less than max seats
    def create_remaining_tables(self):
        people = len(self.unassigned_people)
        leftover = people % self.max_seats
        for i in range(leftover):
            max_seats = self.max_seats - 1
            table = Table(max_seats, i + self.last_id + 1)
            self.add_table(table)
            
            print(table.id)

    def assign_couples_to_tables(self):
        for table in self.tables:
            number = len(table.people)    
            if self.max_seats - 1 >= number:
                for person1 in self.unassigned_people:
                    for person2 in self.unassigned_people:
                        if person1 not in table.people or person2 not in table.people:
                            if person1.name == person2.spouse:
                                table.add_person(person1)
                                table.add_person(person2)
                                self.remove_person(person1)
                                self.remove_person(person2)
            # for person in table.people:
            #     print(person.name)
        # print("singles")