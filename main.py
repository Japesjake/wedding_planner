from Wedding import *

wedding = Wedding()


wedding.start()
wedding.max_seats = wedding.query_max_seats()
wedding.open_csv()
wedding.create_tables()
# wedding.create_main_tables()
# wedding.create_remaining_tables()
# wedding.assign_couples_to_tables()
# wedding.assign_singles_to_tables()

# for table in wedding.tables:
#     if wedding.max_seats > len(table.people):
#         for person in wedding.unassigned_people:
#             table.add_person(person)
#             for person in table.people:
#                 print(person.name, table.id)


# to do #
# assign singles to to remaining seats
# add more entries to input.csv file