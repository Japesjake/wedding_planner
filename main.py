from Wedding import *

wedding = Wedding()


wedding.start()
wedding.max_seats = wedding.query_max_seats()
wedding.open_csv()
wedding.create_tables()
wedding.match_couples()
wedding.assign_couples_to_tables()
wedding.assign_singles_to_tables()

wedding.test()
# to do #

# edit code to consider the situation where 
# there are more leftovers than tables.

# assign singles to to remaining seats
# add more entries to input.csv file