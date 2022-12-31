import shelve

# with shelve.open('shelve_test') as cars:
cars = shelve.open('shelve_test1')

cars['opel'] = 'Germany'
cars['ford'] = 'USA'
cars['mazda'] = 'Japan'
cars['renault'] = 'France'

print(cars['ford'])
print(cars['renault'])
print(cars)
print(type(cars))

ordered_keys_list = list(cars.keys())
ordered_keys_list.sort()

for key in ordered_keys_list:
    print(key + ' ' + cars[key])

for value in cars.values():
    print(value)
print(cars.values())
print(type(cars.values()))

for keys in cars.keys():
    print(keys)
print(cars.keys())
print(type(cars.keys()))

for item in cars.items():
    print(item)
print(cars.items())
print(type(cars.items()))

cars.close()


    # del cars['vaz']
    #
    # cars['kia'] = 'Sout Korea'
    #
    # # for key in cars:
    # #     print(key)
    #
    # for key in cars:
    #     print(key + ': ' + cars[key])

    # while True:
    #     key = input('Please enter a car name: ')
    #     if key == 'quit':
    #         break
    #     country = cars.get(key, "We don't have a " + key)
    #     print(country)

    # while True:
    #     key = input('Please enter a car name: ')
    #     if key == 'quit':
    #         break
    #     if key in cars:
    #         country = cars[key]
    #         print(country)
    #     else:
    #         print('We dont have a ' + key)

    # ordered_keys_list = list(cars.keys())
    # ordered_keys_list.sort()
    #
    # for key in ordered_keys_list:
    #     print(key + ' ' + cars[key])

    # for value in cars.values():
    #     print(value)
    # print(cars.values())
    # print(type(cars.values()))
    #
    # for keys in cars.keys():
    #     print(keys)
    # print(cars.keys())
    # print(type(cars.keys()))
    #
    # for item in cars.items():
    #     print(item)
    # print(cars.items())
    # print(type(cars.items()))


