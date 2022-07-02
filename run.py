from wedding.Wedding import *

wedding = Wedding()

while True:
    wedding.max_seats = wedding.query_max_seats()
    if wedding.max_seats <= 1: continue
    wedding.start()
    wedding.open_csv()
    wedding.create_tables()
    wedding.match_couples()
    wedding.assign_couples_to_tables()
    wedding.assign_singles_to_tables()

    wedding.test_tables()
    wedding.test()