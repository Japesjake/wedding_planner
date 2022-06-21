from Wedding import *

class Table():
    def __init__(self, max_seats, id):
        self.max_seats = max_seats
        self.people = []
        self.id = id
        self.open = False
    def add_person(self, person):
        self.people.append(person)