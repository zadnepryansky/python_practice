# print(1 + 1)
# print('1' + '1')
# age = 23
# print('Jake is ' + str(age) + ' years old.')
# print('Jake is ' + str(23) + ' years old.')

# name = 'Jack'
# age = 23
# name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
# print(name_and_age)
# name_and_age = 'My name is {0}. I\'m {1} years old.'.format('Jack', 23)
# print(name_and_age)
# name_and_age = 'My name is {}. I\'m {} years old.'.format(23, 'Jack')
# print(name_and_age)
#
# week_days = 'The are 7 days in a week :{4},{1},{2},{0},{3},{5},{6}.'\
#     .format('Wednesday','Monday','Tuesday','Thursday','Sunday','Friday', 'Saturday')
# print(week_days)
#
# week_days = 'The are 7 days in a week :{su},{mo},{tu},{we},{th},{fr},{sa}.'\
#     .format(we = 'Wednesday',mo = 'Monday',tu = 'Tuesday',th = 'Thursday'\
#             ,su = 'Sunday',fr = 'Friday',sa = 'Saturday')
# print(week_days)

# float_result = 1000/7
# print(float_result)
# print('The result of division is {0:1.3f}'.format(float_result))
# print("""
# {0:10.2f}{1:10.2f}{2:10.2f}
# {3:10.2f}{4:10.2f}{5:10.2f}
# {6:10.2f}{7:10.2f}{8:10.2f}
# """.format(1.4577, 345.232343, 34.435354,
#            1234.3343,1.4577, 345.232343,
#            34.435354, 1234.3343, 123.3443 ))

name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
print(name_and_age)
name_and_age = f'My name is {name}. I\'m {age} years old.'
print(name_and_age)

print('My name is %s. %s %d years old' % (name,"I'm", age))