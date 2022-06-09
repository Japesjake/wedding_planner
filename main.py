from Wedding import *

wedding = Wedding()


wedding.start()
wedding.max_seats = wedding.queryMaxSeats()
wedding.openCSV()
wedding.create_main_tables()
wedding.create_remaining_tables()
wedding.assign_couples_to_tables()

# for table in wedding.tables:
#     number = len(table.people)    
#     if wedding.max_seats - 1 >= number:
#         for person1 in wedding.unassigned_people:
#             for person2 in wedding.unassigned_people:
#                 if person1 not in table.people or person2 not in table.people:
#                     if person1.name == person2.spouse:
#                         table.addPerson(person1)
#                         table.addPerson(person2)
#                         wedding.removePerson(person1)
#                         wedding.removePerson(person2)


# add more entries