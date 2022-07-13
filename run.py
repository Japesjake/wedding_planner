from wedding.Wedding import *

wedding = Wedding()

wedding.max_seats = wedding.query_max_seats()
wedding.min_seats = wedding.query_min_seats()

wedding.start()
print('This may take a while depending on the number of people and size of each group.')
print('Processing...')
count = 0
while True:
    wedding.create_groups_from_csv()
    wedding.group_singles()
    wedding.create_tables()

    wedding.assign_groups_to_tables()
    count += 1
    if wedding.is_everyone_assigned() or count == 100:
    #     pass
    # if True:
        break

if count == 100:
    print('Process timed out. There may not be a possible arrangement of groups. Try changing the number of seats at each table or changing the people in groups.')
# wedding.test_groups()

wedding.test_tables()
wedding.full_test()