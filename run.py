from wedding.Wedding import *
import time

wedding = Wedding()

wedding.max_seats = wedding.query_for_seats("MAX")
wedding.min_seats = wedding.query_for_seats("MINIMUM")
# wedding.max_seats = 8
# wedding.min_seats = 5


wedding.start()
print('This may take a while depending on the number of people and size of each group.')
print('Processing...')
count = 0
start = time.perf_counter()
while True:
    wedding.create_groups_from_csv()
    wedding.group_singles()
    wedding.create_tables()

    wedding.assign_groups_to_tables()
    count += 1
    end = time.perf_counter()
    time_passed = end - start
    if wedding.is_everyone_assigned() or time_passed > 10:
        break

if time_passed < 10:
    wedding.print_tables()
    wedding.print_names()
else: 
    print('Process timed out. There may not be a possible arrangement of groups. Try increasing the max seats per table, or decreasing the size of some groups')
# wedding.test_groups()
# print(wedding.return_total_num_unassigned_people())