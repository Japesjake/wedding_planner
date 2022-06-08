class Wedding:
    def __init__(self):
        self.tables = []
        self.unassigned_people = []
        self.seats = 0
    def addTable(self, table):
        self.tables.append(table)
    def addPerson(self, person):
        self.unassigned_people.append(person)

    def query_max_seats(self):
        while True:
            # seats = input("Please enter the maximum number of people per table: ")
            seats = 8

            try: seats = int(seats)
            except: print("please enter an integer")
            if isinstance(seats, int): return seats

    def start(self):
        while True:
            # start = input("Open up 'input.csv' in the program directory and input the name, age and spouse (if they have one) of all the guests. Please refer to 'input_example.csv' for an example input. Once you entered all the infomation into 'input.csv' type 'start' and press enter: ")
            start = "start"
            if start == "start": return None
