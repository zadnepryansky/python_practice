# Method Resolution Order (MRO)
#    A
#   / \
#  B   C
#   \ /
#    D

class A:
    def some_method(self):
        print('Method of class A')


class B(A):

    def some_method(self):
        print('Method of class B')


class C(A):

    def some_method(self):
        print('Method of class C')


class D(B, C):

    def some_method(self):
        print('Method of class D')

# __mro__, mro(), help()


print(D.__mro__)
print(D.mro())
print(help(D))
some_object = D()
some_object.some_method()