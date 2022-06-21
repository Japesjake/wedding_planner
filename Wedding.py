import csv
from Person import *
from Table import *

class Wedding:
    def __init__(self):
        self.unassigned_people = []
        self.couples = []
        self.tables = []
    def add_table(self, table):
        self.tables.append(table)
    def remove_table(self, table):
        self.tables.remove(table)
    def couple_table(self, table):
        self.coupled_tables.append(table)
    def add_person(self, person):
        self.unassigned_people.append(person)
    def remove_person(self, person):
        self.unassigned_people.remove(person)
    def add_couple(self, couple):
        self.couples.append(couple)
    def remove_couple(self, couple):
        self.couples.remove(couple)

    # asks for max seats per table.
    def query_max_seats(self):
        while True:
            # seats = input("Please enter the maximum number of people per table: ")
            seats = 7#

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
            if name == "NAME": continue
            self.add_person(Person(name, age, spouse))

    def round_up(self, numerator, divisor):
        return int((numerator // divisor) + (numerator % divisor > 0))

    def is_more_required(self, num1, num2, num3):
        if self.unassigned_people - num > num - 2:
            return True

    def create_tables(self):
        people = len(self.unassigned_people)
        seats = self.max_seats
        tables = self.round_up(people, seats)
        for i in range(self.max_seats - 2, self.max_seats):
            if self.is_more_required(i):
                for j in range(self.max_seats - 2, self.max_seats):
                    if self.is_more_required(j):
                        for k in range(self.max_seats - 2, self.max_seats):
                            if i + j + k == people:
                                for id in range(tables):
                                    table = Table(, id)
                                    self.add_table(table)



        # for i in range(tables):
        #     table = Table(self.seats, i)
        #     self.add_table(table)

    def match_couples(self):
        for person1 in self.unassigned_people:
            for person2 in self.unassigned_people:
                if person1.name == person2.spouse:
                    self.add_couple((person1, person2))
                    
    def is_even(self, number):
        if number % 2 == 0: return True

    def assign_couples_to_tables(self):
        even = self.is_even(self.max_seats)
        for couple in self.couples:
            for person in couple:
                for table in self.tables:
                    if person in self.unassigned_people:
                        if even and table.seats >= len(table.people):
                            self.remove_person(person)
                            table.add_person(person)
                        elif not even and table.max_seats >= len(table.people) + 2:
                            self.remove_person(person)
                            table.add_person(person)
                            
                            


    def assign_singles_to_tables(self):
        for person in self.unassigned_people:
            for table in self.tables:
                if table.max_seats > len(table.people):
                    if person in self.unassigned_people:
                        self.remove_person(person)
                        table.add_person(person)


    def test_people(self):
        for table in self.tables:
            for person in table.people:
                print(person.name, ":", table.id)

    def test_seats(self):

