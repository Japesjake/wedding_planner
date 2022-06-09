from Wedding import *

class Table():
    def __init__(self, seats):
        self.people = []
        self.seats = seats
    def addPerson(self, person):
        self.people.append(person)
    def isFull(self, table):
        if len(table.people) >= self.max_seats: return True
        return False