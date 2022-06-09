import csv
from Person import *
from Table import *

class Wedding:
    def __init__(self):
        self.tables = []
        self.unassigned_people = []
        self.max_seats = 0
    def addTable(self, table):
        self.tables.append(table)
    def addPerson(self, person):
        self.unassigned_people.append(person)
    def removePerson(self, person):
        self.unassigned_people.remove(person)
    # asks for max seats per table.
    def queryMaxSeats(self):
        while True:
            # seats = input("Please enter the maximum number of people per table: ")
            seats = 8#

            try: seats = int(seats)
            except: print("please enter an integer")
            if isinstance(seats, int): return seats

    def start(self):
        while True:
            # start = input("Open up 'input.csv' in the program directory and input the name, age and spouse (if they have one) of all the guests. Please refer to 'input_example.csv' for an example input. Once you entered all the infomation into 'input.csv' type 'start' and press enter: ")
            start = "start"#
            if start == "start": return None
    def openCSV(self):
        csv_file = open('input.csv', 'r')
        csv_reader = csv.reader(csv_file)
        for name, age, spouse in csv_reader:
            # print(name, age, spouse)

            self.addPerson(Person(name, age, spouse))
            if name == "NAME": continue

    # Creates table with max seats
    def create_main_tables(self):
        people = len(self.unassigned_people)
        main = people // self.max_seats
        for i in range(main):
            table = Table(self.max_seats)
            self.addTable(table)

    # Creates tables with less than max seats
    def create_remaining_tables(self):
        people = len(self.unassigned_people)
        leftover = people % self.max_seats
        for i in range(leftover):
            table = Table(self.max_seats - 1)
            self.addTable(table)

    def assign_couples_to_tables(self):
        for table in self.tables:
            number = len(table.people)    
            if self.max_seats - 1 >= number:
                for person1 in self.unassigned_people:
                    for person2 in self.unassigned_people:
                        if person1 not in table.people or person2 not in table.people:
                            if person1.name == person2.spouse:
                                table.addPerson(person1)
                                table.addPerson(person2)
                                self.removePerson(person1)
                                self.removePerson(person2)
        for table in self.tables:
            for person in table.people:
                print(person.name)