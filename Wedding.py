import csv
import random
from Person import *
from Table import *

class Wedding:
    def __init__(self):
        self.unassigned_people = []
        self.couples = []
        self.tables = []
    def add_table(self, table):
        self.tables.append(table)
    def add_person(self, person):
        self.unassigned_people.append(person)
    def remove_person(self, person):
        self.unassigned_people.remove(person)
    def add_couple(self, couple):
        self.couples.append(couple)
    def remove_couple(self, couple):
        self.couples.remove(couple)

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
    
    def open_csv(self):
        csv_file = open('input.csv', 'r')
        csv_reader = csv.reader(csv_file)
        for name, age, spouse in csv_reader:
            if name == "NAME": continue
            self.add_person(Person(name, age, spouse))

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

    def match_couples(self):
        people_coupled = []
        for person1 in self.unassigned_people:
            people_coupled.append(person1)
            for person2 in self.unassigned_people:
                if person1.name == person2.spouse and person2 not in people_coupled:
                    self.add_couple((person1, person2))

    def assign_couples_to_tables(self):
        for table in self.tables:
            broken = False
            for couple in self.couples:
                i = 0
                if broken: break
                for person in couple:
                    i += 1
                    if person in self.unassigned_people:
                        self.remove_person(person)
                        table.add_person(person)
                        # print(person.name, ":", "id = ", table.id, "couple: = ", i)
                    if table.max_seats <= len(table.people) + 1 and i == 2:
                        broken = True
                        if broken: break
                    
    
    def assign_singles_to_tables(self):
        for table in self.tables:
            people = list(self.unassigned_people)
            for person in people:
                if table.max_seats > len(table.people):
                    if person in self.unassigned_people:
                        self.remove_person(person)
                        table.add_person(person)

    def test_tables(self):
        for table in self.tables:
            print("table" ,table.id, "has", table.max_seats, "seats")
    
    def test(self):
        print()
        for table in self.tables:
            print()
            print("table", table.id)
            for person in table.people:
                print(person.name)

