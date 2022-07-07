from wedding.Wedding import *

wedding = Wedding()

# while True:
wedding.max_seats = wedding.query_max_seats()
# if wedding.max_seats <= 1: continue
wedding.start()
wedding.create_groups_from_csv()
wedding.update_numbers_in_groups()
wedding.create_tables()

wedding.test_groups()

# wedding.test_tables()
# wedding.test()