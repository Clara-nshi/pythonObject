class A(object):
    pass


class B(object):
    pass


class C(A):
    pass


class D(B):
    pass


class E(C, D):
    pass


print(E.mro())
print(E.__mro__)
# [<class '__main__.E'>,
# <class '__main__.C'>,
# <class '__main__.A'>,
# <class '__main__.D'>,
# <class '__main__.B'>,
# <class 'object'>]
