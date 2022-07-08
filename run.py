from wedding.Wedding import *

wedding = Wedding()

# while True:
wedding.max_seats = wedding.query_max_seats()
# if wedding.max_seats <= 1: continue
wedding.start()
wedding.create_groups_from_csv()
while True:
    wedding.create_tables()
    wedding.assign_groups_to_tables()
    if True:
    # if wedding.return_total_num_unassigned_people() == 0:
        break


# wedding.create_tables()

# wedding.test_groups()

# wedding.test_tables()
# wedding.full_test()
# wedding.test()