from Wedding import *
from Table import *
from Person import *
from Group import *
import csv

wedding = Wedding()


wedding.start()
max_seats = wedding.query_max_seats()


csv_file = open('input.csv', 'r')
csv_reader = csv.reader(csv_file)
for name, age, spouse in csv_reader:
    if name == "NAME": continue

    print(name, age, spouse)

    wedding.addPerson(Person(name, age, spouse))


length = len(wedding.unassigned_people)
# for i in
table = Table()
wedding.addTable(table)
for person1 in wedding.unassigned_people:
    for person2 in wedding.unassigned_people:
        if person1.name == person2.spouse:

            table.addPerson(person1)
            table.addPerson(person2)
