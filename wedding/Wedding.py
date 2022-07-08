import csv
import random
from person.Person import *
from table.Table import *
from group.Group import *

class Wedding:
    def __init__(self):
        self.unassigned_groups = []
        self.tables = []
    def add_table(self, table):
        self.tables.append(table)
    def add_group(self, group):
        self.unassigned_groups.append(group)
    def remove_group(self, group):
        self.unassigned_groups.remove(group)

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
            # start = input("Open up 'input.csv' in the program directory and input the name of guests (put a space between groups)""
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
                person = Person(name)
                group.add_person(person)

    def return_num_people_at_table(self, table):
        total = 0
        for group in table.groups:
            total += len(group.people)
        return total

    def return_total_num_assigned_people(self):
        total = 0
        for table in self.tables:
            for group in table.groups:
                total += len(group.people)
        return total

#
    def return_total_num_unassigned_people(self):
        total = 0
        for group in self.unassigned_groups:
            total += len(group.people)
        return total
#

    def round_up(self, numerator, divisor):
        return int((numerator // divisor) + (numerator % divisor > 0))

    def create_tables(self):
        total_people = self.return_total_num_unassigned_people()
        tables = self.round_up(total_people, self.max_seats)
        broken = False
        while not broken:
            people = 0
            self.tables = []
            for i in range(1, tables + 1):
                int = random.randint(self.max_seats - 4, self.max_seats)
                table = Table(int, i)
                self.add_table(table)
                people += int
                if people == total_people:
                    broken = True
                    break

    def assign_groups_to_tables(self):
        for table in self.tables:
            for group in self.unassigned_groups:
                people = self.return_num_people_at_table(table)
                if len(group.people) + people <= table.max_seats and group in self.unassigned_groups:
                    table.add_group(group)
                    self.remove_group(group)
        # print("unassigned: ", self.return_total_num_unassigned_people())
        # print("assigned: ", self.return_total_num_assigned_people())

    def test_groups(self):
        for group in self.groups:
            print(group.id)
            for person in group.people:
                print(person.name)
    
    def test_tables(self):
        for table in self.tables:
            print('table: ', table.id, "seats: ", table.max_seats)

    def full_test(self):
        for table in self.tables:
            print(table.id)
            for group in table.groups:
                for person in group.people:
                    print(person.name)