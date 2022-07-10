from wedding.Wedding import *

wedding = Wedding()

wedding.max_seats = wedding.query_max_seats()
wedding.min_seats = wedding.query_min_seats()

wedding.start()

while True:
    wedding.create_groups_from_csv()
    wedding.create_tables()

    wedding.assign_groups_to_tables()
    if wedding.is_everyone_assigned():
        break

# wedding.test_groups()

wedding.test_tables()
wedding.full_test()