# If we have an error - except block fires and else doesn't fire
# If we haven't an error - else block fires and except doesn't fire
# Finally block fires anyway



# while True:
#     try:
#         number = int(input('Enter some number: '))
#         print(number / 2)
#     except:
#         print('You have to enter a number!')
#     else:
#         print('Good job! This is a number')
#         break
#     finally:
#         print('Finally block')
#
# print('Code after error handling')

def divide(x,y):
    try:
        return x / y
    except ZeroDivisionError as e:
        print('You can\'t divide by zero!')
        print(e)
    except TypeError as e:
        print('x and y mus be numbers')
        print(e)
    else:
        print('x was divided by y')
    finally:
        print('Finally block')


print(divide(4, 'jj'))
# print(divide(4, 'w'))
