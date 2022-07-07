class Group:
    def __init__(self, id):
        self.people = []
        self.id = id
        self.number = 0
    def add_person(self, person):
        self.people.append(person)
    def update_number(self):
        self.number = len(self.people)
