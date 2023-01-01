# int_num = 50
# float_num = 7.5
#
# # print(int_num * float_num)
#
# print(int_num.__mul__(float_num))
# # NotImplemented

# print(float_num.__rmul__(int_num))

float_num = 50.5
str_val = 'abc'

# print(str_val * int_num)

print(float_num.__mul__(str_val))
# NotImplemented

print(str_val.__rmul__(float_num))