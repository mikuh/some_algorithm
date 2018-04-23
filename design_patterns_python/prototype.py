import copy

class Prototype(object):
    """A prototype base class
    """
    def clone(self):
        return copy.deepcopy(self)


class Register(Prototype):
    def __init__(self, names=[]):
        self.names = names



class MetaPrototype(type):
    """A metaclass for Prototypes
    """
    def __init__(cls, *args):
        type.__init__(cls, *args)
        cls.clone = lambda self: copy.deepcopy(self)


class PrototypeM(metaclass=MetaPrototype):
    pass


class ItemCollection(PrototypeM):
    def __init__(self, items=[]):
        self.items = items

if __name__ == '__main__':
    r1 = Register(names=['aaa', 'bbb', 'ccc'])
    r2 = r1.clone()
    print(r1)
    print(r2)


    i1 = ItemCollection(items=['apple', 'google', 'facebook'])
    print('i1', i1)
    i2 = i1.clone()
    print('i2', i2)

    print(i1 is i2)