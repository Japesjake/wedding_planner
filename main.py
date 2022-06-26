from Wedding import *

wedding = Wedding()

wedding.max_seats = wedding.query_max_seats()
wedding.start()
wedding.open_csv()
wedding.create_tables()
wedding.match_couples()
wedding.assign_couples_to_tables()
wedding.assign_singles_to_tables()

wedding.test_tables()
wedding.test()
# to do #

# add web compatibility