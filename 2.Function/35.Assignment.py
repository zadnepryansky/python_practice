# def is_cat_here(*args):
#     return 'cat' in str(args).lower()
#
# print(is_cat_here('cat', 'dog', 'pig'))

# def is_item_here(item, *args):
#     return item in args
#
# print(is_item_here(12, 12, 10, 11))

def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print('My favorite color is ' + str(my_color) +
              ', but ' + kwargs['blue'] + ' is also pretty good!')
    else:
        print('My favorite color is ' + str(my_color) +
              ', what is your favorite color?')

your_favorite_color()
