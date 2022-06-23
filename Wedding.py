import csv
import random
from decimal import ROUND_UP
from Person import *
from Table import *

class Wedding:
    def __init__(self):
        self.unassigned_people = []
        self.couples = []
        self.tables = []
        self.possible_seats = []
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
    def make_add_table(self, seats, id):
        table = Table(seats, id)
        self.add_table(table)
    def add_possible_seats(self, seats):
        self.possible_seats.append(seats)

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

    # Returns a combination of seat amounts per table,
    # which add up to the amount of people.
    def make_poss_seats(self):
        people = len(self.unassigned_people)
        max = self.max_seats
        r = range(max - 2, max + 1)
        seats_list = []
        max_tables = self.round_up(people, max)
        while sum(seats_list) != people:
            if max_tables == len(seats_list):
                seats_list = []            
            ran = random.randint(max - 2, max)
            seats_list.append(ran)
        return seats_list

    def create_tables(self):
        id = 0
        numbers = self.make_poss_seats()
        # print(numbers)
        for seats in numbers:
            table = Table(seats, id)
            self.add_table(table)
            # print(table.seats)
            id += 1

    def match_couples(self):
        for person1 in self.unassigned_people:
            for person2 in self.unassigned_people:
                if person1.name == person2.spouse:
                    self.add_couple((person1, person2))
                    
    def is_even(self, number):
        if number % 2 == 0: return True
        else: return False

    def assign_couples_to_tables(self):
        for couple in self.couples:
            for person in couple:
                for table in self.tables:
                    even = self.is_even(table.seats)
                    if person in self.unassigned_people:
                        if even and table.seats >= len(table.people):
                            self.remove_person(person)
                            table.add_person(person)
                        elif not even and table.seats >= len(table.people) + 1:
                            self.remove_person(person)
                            table.add_person(person)
                        # print(person.name, table.id)

    # def assign_couples_to_tables

    def assign_singles_to_tables(self):
        for person in self.unassigned_people:
            for table in self.tables:
                actual_people = len(table.people)
                if table.seats > actual_people:
                    if person in self.unassigned_people:
                        self.remove_person(person)
                        table.add_person(person)

    def test_people(self):
        for table in self.tables:
            for person in table.people:
                print(person.name, ":", table.id)

