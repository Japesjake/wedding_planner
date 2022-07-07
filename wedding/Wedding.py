import csv
import random
from person.Person import *
from table.Table import *
from group.Group import *

class Wedding:
    def __init__(self):
        self.unassigned_people = []
        self.groups = []
        self.tables = []
    def add_table(self, table):
        self.tables.append(table)
    def add_person(self, person):
        self.unassigned_people.append(person)
    def remove_person(self, person):
        self.unassigned_people.remove(person)
    def add_group(self, group):
        self.groups.append(group)

    # gets user input for max seats per table.
    def query_max_seats(self):
        while True:
            # seats = input("Please enter the maximum number of seats per table: ")
            seats = 7

            try: seats = int(seats)
            except: print("please enter an integer.")
            if isinstance(seats, int): return seats

    def start(self):
        while True:
            # start = input("Open up 'input.csv' in the program directory and input the name, age and spouse (if they have one) of all the guests. Please refer to 'input_example.csv' for an example input. Once you entered all the infomation into 'input.csv' type 'start' and press enter: ")
            start = "start"
            if start == "start": return None

    def create_groups_from_csv(self):
        csv_file = open('wedding_seater/input.csv', 'r')
        csv_reader = csv.reader(csv_file)
        id = 0
        for name in csv_reader:
            if not name or name == ['NAME']:
                id += 1
                group = Group(id)
                self.add_group(group)
            if name and name != ['NAME']:
                group.add_person(Person(name))

    def round_up(self, numerator, divisor):
        return int((numerator // divisor) + (numerator % divisor > 0))

    def create_tables(self):
        num_people = len(self.unassigned_people)
        tables = self.round_up(num_people, self.max_seats)
        broken = False
        while not broken:
            people = 0
            self.tables = []
            for i in range(1, tables + 1):
                int = random.randint(self.max_seats - 2, self.max_seats)
                table = Table(int, i)
                self.add_table(table)
                people += int
                if people == len(self.unassigned_people):
                    broken = True
                    break
    
    def update_num_people_in_groups(self):
        for group in self.groups:
            self.number = len(group.people)

    def assign_groups_to_tables(self):
        for table in self.tables:
            for group in self.groups:
                if group.number < 
                    
    # def test_tables(self):
    #     for table in self.tables:
    #         print("table" ,table.id, "has", table.max_seats, "seats")
    
    # def test(self):
    #     print()
    #     for table in self.tables:
    #         print()
    #         print("table", table.id)
    #         for person in table.people:
    #             print(person.name)

    def test_groups(self):
        for group in self.groups:
            print(group.id)
            print('number: ', group.number)
            for person in group.people:
                print(person.name)