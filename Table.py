from Wedding import *

class Table():
    def __init__(self, seats, id):
        self.seats = seats
        self.people = []
        self.id = id
        self.open = False
    def add_person(self, person):
        self.people.append(person)