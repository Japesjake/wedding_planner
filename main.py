import Wedding
import Table
from Person import *
import csv



csv_file = open('input.csv', 'r')
csv_reader = csv.reader(csv_file)
for name, age, spouse in csv_reader:
    if name == "NAME": continue
    print(name, age, spouse)
        Person(name, age, spouse)