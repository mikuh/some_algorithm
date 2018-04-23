class Brog(object):
    __shared_state = {}
    def __init__(self):
        print(Brog.__shared_state)
        self.__dict__ = self.__shared_state


class IBrog(Brog):
    def __init__(self):
        Brog.__init__(self)
        self.state = 'init'

    def __str__(self):
        return self.state

class MyBrog(IBrog):
    pass

if __name__ == '__main__':
    i1 = IBrog()
    i2 = MyBrog()

    print('i1:{}, i2:{}'.format(i1, i2))
    i1.state = 'running'
    print('i1:{}, i2:{}'.format(i1, i2))

    i1.x = 'test'
    print(i2.x)