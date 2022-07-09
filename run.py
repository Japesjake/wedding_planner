from wedding.Wedding import *
import copy

wedding = Wedding()

wedding.max_seats = wedding.query_max_seats()
wedding.max_seats = wedding.query_min_seats()

wedding.start()

# is_run = False
while True:
    # if is_run: wedding.unassigned_people = wedding.unassigned_people_before
    # else: wedding.unassigned_people = wedding.return_total_num_unassigned_people()
    wedding.create_groups_from_csv()
    wedding.create_tables()
    wedding.assign_groups_to_tables()
    # is_run = True
    if wedding.is_everyone_assigned():
        break

# wedding.test_groups()

wedding.test_tables()
wedding.full_test()