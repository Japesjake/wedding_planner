import csv
from Person import *
from Table import *

class Wedding:
    def __init__(self):
        self.unassigned_people = []
        self.couples = []
        self.tables = []
        self.max_seats = 0
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

    def round_up(self, numerator, divisor):
        return int((numerator // divisor) + (numerator % divisor > 0))

    # Creates tables
    def create_tables(self):
        num_people = len(self.unassigned_people)
        tables = self.round_up(num_people, self.max_seats)
        for i in range(tables):
            table = Table(self.max_seats, i)
            self.add_table(table)
            # print(table.id, ":", table.max_seats)

    def match_couples(self):
        for person1 in self.unassigned_people:
            for person2 in self.unassigned_people:
                if person1.name == person2.spouse:
                    self.add_couple((person1, person2))
        # for couple in self.couples:
        #     for person in couple:
        #         print(person.name)

    def assign_couples_to_tables(self):
        for couple in self.couples:
            for person in couple:
                for table in self.tables:
                    if person in self.unassigned_people:
                        if table.max_seats >= len(table.people) + 1:
                            self.remove_person(person)                                
                            table.add_person(person)
                        
        for table in self.tables:
            for person in table.people:
                print(person.name)






    # def assign_couples_to_tables(self):
    #     for table in self.tables:
    #         if table.max_seats >= len(table.people) + 1:
    #             for couple in self.couples:
    #                 self.remove_couple(couple)
    #                 for person in couple:
    #                     table.add_person(person)
            # print(table)