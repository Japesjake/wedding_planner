import csv
import random
from person.Person import *
from table.Table import *
from group.Group import *

class Wedding:
    def __init__(self):
        self.unassigned_groups = []
        self.unassigned_singles = []
        self.tables = []
    def add_table(self, table):
        self.tables.append(table)
    def add_group(self, group):
        self.unassigned_groups.append(group)

    ### UTILITY METHODS ###

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

    def return_total_num_unassigned_people(self):
        total = 0
        for group in self.unassigned_groups:
            total += len(group.people)
        for group in self.unassigned_singles:
            total += len(group.people)
        return total

    def return_total_num_seats(self):
        num = 0
        for table in self.tables:
            num += table.max_seats
        return num

    def is_everyone_assigned(self):
        if self.return_total_num_unassigned_people() == 0: return True

    def round_up(self, numerator, divisor):
        return int((numerator // divisor) + (numerator % divisor > 0))

    ### MAIN METHODS ##

    # gets user input for maximum or minimum (depends on string) seats per table.
    def query_for_seats(self, string):
        while True:
            seats = input(f"Please enter the {string} number of seats per table: ")
            try: 
                seats = int(seats) 
            except: 
                print("Please enter an integer.")
                continue
            if seats > 0: return seats 
            else: print("Please enter a positive integer.")

    def start(self):
        while True:
            # start = input("Open up 'input.csv' in the program directory and input the name of guests (put a space between groups)""
            start = "start"
            if start == "start": return None

    def create_groups_from_csv(self):
        self.unassigned_groups = []
        csv_file = open('input.csv', 'r')
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
        random.shuffle(self.unassigned_groups)

    def group_singles(self):
        self.unassigned_singles = []
        self.unassigned_groups_static = list(self.unassigned_groups)
        for group in self.unassigned_groups_static:
            if len(group.people) == 1:
                self.unassigned_groups.remove(group)
                self.unassigned_singles.append(group)     

    def create_tables(self):
        self.unassigned_people = self.return_total_num_unassigned_people()
        num_tables = self.round_up(self.unassigned_people, self.max_seats)
        while True:
            self.tables = []
            for id in range(1, num_tables + 1):
                seats = random.randint(self.min_seats, self.max_seats)
                self.add_table(Table(seats, id))
            total_num_seats = self.return_total_num_seats()
            if total_num_seats > self.unassigned_people: continue
            elif total_num_seats == self.unassigned_people: break

    def assign_groups_from_list(self, list):
        for table in self.tables:
            for group in list:
                people = self.return_num_people_at_table(table)
                if len(group.people) + people <= table.max_seats and group in list:
                    table.add_group(group)
                    list.remove(group)

    def assign_groups_to_tables(self):
        self.assign_groups_from_list(self.unassigned_groups)
        self.assign_groups_from_list(self.unassigned_singles)
    
    def print_tables(self):
        for table in self.tables:
            print('table ', table.id, 'has ', table.max_seats, ' seats')

    def print_names(self):
        for table in self.tables:
            print(table.id)
            for group in table.groups:
                for person in group.people:
                    print(person.name)

    # Testing Methods #

    def print_groups(self):
        for group in self.unassigned_groups:
            print("group ", group.id, )
            for person in group.people:
                print(person.name)

        for group in self.unassigned_singles:
            print("group ", group.id, )
            for person in group.people:
                print(person.name)   

    def print_numbers(self):
        print("unassigned: ", self.return_total_num_unassigned_people())
        print("assigned: ", self.return_total_num_assigned_people())