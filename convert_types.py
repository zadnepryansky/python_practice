# print('10' + 2)  # can only concatenate str (not "int") to str
# print(10 + '2')  # unsupported operand type(s) for +: 'int' and 'str'


int_num = 5
float_num = 4.5
print(int_num + float_num)
print(int_num.__add__(float_num))
print(float_num + int_num)
print(float_num.__radd__(int_num))

bool_val = True
int_val = 7
print(bool_val + int_val)
print(int_val + bool_val)