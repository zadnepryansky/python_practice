import shelve

with shelve.open('shelve_test') as cars:
    cars['opel'] = 'Germany'
    cars['ford'] = 'USA'
    cars['mazda'] = 'Japan'
    cars['renault'] = 'France'
    cars['vaz'] = 'parasha'

    print(cars['ford'])
    print(cars['renault'])
    print(cars['opel'])
    print(cars['vaz'])

    del cars['vaz']

    for key in cars:
        print(key)

