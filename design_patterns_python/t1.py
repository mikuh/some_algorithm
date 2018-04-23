class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        print('name:', name)
        print('bases:', bases)
        print('attrs:', attrs)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    id = 100
    def save(self):
        print(getattr(self, 'id', 'haha'))

L = MyList()
L.save()