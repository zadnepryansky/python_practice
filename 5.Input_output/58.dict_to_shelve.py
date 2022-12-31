import shelve

university = shelve.open('university_files')
# university['schedules'] = {
#
#         'monday_schedule': ['Math', 'English Language', 'System programing', 'Python'],
#         'tuesday_schedule': ['English Language', 'HTML', 'Python', 'Football'],
#         'wednesday_schedule': ['Physics', 'English Language', 'Python'],
#         'thursday_schedule': ['Math', 'Chemistry', 'Java'],
#         'friday_schedule': ['Running', 'Math',  'Python']
#     }
# university['tutors'] = {
#         'Math': ['Jack White', 'Jim Black'],
#         'Python': ['YouRa Allakhverdov', 'Jane Smith']
#     }

print(university['schedules']['wednesday_schedule'])
print(university['tutors']['Math'])

university.close()

# university = {
#     'schedules': {
#         'monday_schedule': ['Math', 'English Language', 'System programing', 'Python'],
#         'tuesday_schedule': ['English Language', 'HTML', 'Python', 'Football'],
#         'wednesday_schedule': ['Physics', 'English Language', 'Python'],
#         'thursday_schedule': ['Math', 'Chemistry', 'Java'],
#         'friday_schedule': ['Running', 'Math',  'Python']
#     },
#
#     'tutors': {
#         'Math': ['Jack White', 'Jim Black'],
#         'Python': ['YouRa Allakhverdov', 'Jane Smith']
#     }
# }
#
# print(university['schedules']['wednesday_schedule'])
# print(university['tutors']['Math'])
