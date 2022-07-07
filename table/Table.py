# from wedding.Wedding import *

class Table():
    def __init__(self, max_seats, id):
        self.max_seats = max_seats
        self.num_seats = 0
        self.groups = []
        self.id = id
        self.open = False
    def add_group(self, group):
        self.groups.append(group)
    def update_number_of_seats(self):
        for group in self.groups:
            number = 0
            number += group.number
        self.num_seats = number