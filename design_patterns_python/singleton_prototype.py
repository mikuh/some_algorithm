import copy
class MetaSingLetonPrototype(type):

    def __init__(self, *args):
        print('__init__')
        # super().__init__(self)
        self.instance = None
        self.clone = lambda a: copy.deepcopy(self.instance)
        print('__new__')



    def __call__(self, *args, **kwargs):
        print('__call__')
        if not self.instance:
            self.instance = super().__call__(self)
        return self.instance




class PrototypeM(metaclass=MetaSingLetonPrototype):
    # def __init__(self):
    #     print('PrototypeM __init__')
    pass


class ItemCollection(PrototypeM):
    def __init__(self, items=[]):
        print('ItemCollection __init__')
        # super().__init__()
        self.items = items



i1 = ItemCollection(items=['apple', 'google', 'facebook'])
print('i1', i1, i1.instance)
i2 = i1.clone()
print('i2', i2, i2.instance)

print(i1 is i2)

i3 = ItemCollection(items=['apple', 'google', 'facebook'])
print(i1 is i3)