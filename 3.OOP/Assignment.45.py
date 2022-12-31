class Chain:

    def __init__(self, number_of_items):
        self.number_of_items = number_of_items

    def __str__(self):
        return 'Chain with ' + str(self.number_of_items) + ' items'

    def __len__(self):
        return self.number_of_items


number_1 = Chain(150)
number_2 = Chain(200)

print(number_1)
print(number_2)

print(len(number_1))
print(len(number_2))
