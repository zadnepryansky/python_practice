
def get_week_day(day):
    week = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
    ]
    for day in week:
        yield day


current_day = get_week_day('Sunday')
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())




