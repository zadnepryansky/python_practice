while True:
    try:
        number = eval(input('Input some data: '))
        res = 3 / number
        print(res)
    except NameError:
        print(f'Please input a number')
    except ZeroDivisionError:
        print(f'Input somthing another than 0 ')
    except Exception as e:
        print(f'Problem with {e}')

