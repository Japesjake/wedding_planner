# from wedding.Wedding import *

class Table():
    def __init__(self, max_seats, id):
        self.max_seats = max_seats
        self.groups = []
        self.id = id
    def add_group(self, group):
        self.groups.append(group)
