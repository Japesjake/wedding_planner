from Wedding import *

class Table():
    def __init__(self, max_people, id):
        self.max_people = max_people
        self.people = []
        self.id = id
    def add_person(self, person):
        self.people.append(person)
    def is_full(self, table):
        if len(table.people) >= self.max_seats: return True
        return False
    