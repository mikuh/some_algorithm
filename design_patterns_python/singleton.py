"""
单例是只有一个实例和明确定义访问点的类
"""
class Singleton(object):
    """Singleton in Python
    """
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance


class MetaSingleton(type):
    """A type for Singleton classes(overrides __call__)
    """
    def __init__(cls, *args):
        print(cls, "__init__ method called with args", args)
        type.__init__(cls, *args)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            print(cls, "creating instance", args, kwargs)
        return cls.instance

class SingletonM(metaclass=MetaSingleton):
    pass


def test_single(cls):
    return cls() == cls()

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print(s1 == s2)

    print(test_single(SingletonM))