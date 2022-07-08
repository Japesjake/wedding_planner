class Group:
    def __init__(self, id):
        self.people = []
        self.id = id
        self.num_people = 0
    def add_person(self, person):
        self.people.append(person)
    def update_number(self):
        self.num_people = len(self.people)