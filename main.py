from Wedding import *
from Table import *
from Person import *
import csv

while True:
    num = input("Please enter the maximum number of people per table: ")
    num = int(num)
    if isinstance(num, int): break
while True:
    start = input("Firstly, open up 'input.csv' in the program directory and input the name, age and spouse (if they have one) of all the guests. Please refer to 'input_example.csv' for an example input. Once you entered all the infomation into 'input.csv' type 'start' and press enter: ")
    if start == "start": break

wedding = Wedding()

csv_file = open('input.csv', 'r')
csv_reader = csv.reader(csv_file)
for name, age, spouse in csv_reader:
    if name == "NAME": continue
    print(name, age, spouse)
    wedding.addPerson(Person(name, age, spouse))