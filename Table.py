from Wedding import *

class Table(Wedding):
    def __init__(self):
        self.people = []
        self.seats = 0
        # super().__init__(max_seats)
    def addPerson(self, person):
        self.people.append(person)
    def isFull(self, table):
        if len(table.people) >= self.max_seats: return True
        return False