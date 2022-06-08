from Wedding import *
from Table import *
from Person import *
from Group import *
import csv

wedding = Wedding()

while True:
    # seats = input("Please enter the maximum number of people per table: ")
    seats = 8

    try: wedding.seats = int(seats)
    except: print("please enter an integer")
    if isinstance(wedding.seats, int): break
while True:
    # start = input("Firstly, open up 'input.csv' in the program directory and input the name, age and spouse (if they have one) of all the guests. Please refer to 'input_example.csv' for an example input. Once you entered all the infomation into 'input.csv' type 'start' and press enter: ")
    start = "start"

    if start == "start": break



csv_file = open('input.csv', 'r')
csv_reader = csv.reader(csv_file)
for name, age, spouse in csv_reader:
    if name == "NAME": continue

    # print(name, age, spouse)

    wedding.addPerson(Person(name, age, spouse))
length = len(wedding.unassigned_people)
table = Table()
wedding.addTable(table)
for person1 in wedding.unassigned_people:
    for person2 in wedding.unassigned_people:
        if person1.name == person2.spouse:

            table.addPerson(person1)
            table.addPerson(person2)
