from abc import ABCMeta, abstractmethod

class EmployeeProxy(object):
    count = 0

    def __new__(cls, *args, **kwargs):
        instance = super(EmployeeProxy, cls).__new__(cls)
        cls.incr_count()
        return instance

    def __init__(self, employee):
        self.employee = employee

    @classmethod
    def incr_count(cls):
        cls.count += 1

    @classmethod
    def decr_count(cls):
        cls.count -=1

    @classmethod
    def get_count(cls):
        return cls.count

    def __str__(self):
        return str(self.employee)

    def __getattr__(self, name):
        return getattr(self.employee, name)

    def __del__(self):
        self.decr_count()


class EmployeeProxyFactory(object):
    @classmethod
    def create(cls, name, *args):
        name = name.lower().strip()

        if name == 'engineer':
            return EmployeeProxy(Engineer(*args))
        elif name == 'account':
            return EmployeeProxy(Accountant(*args))
        elif name == 'admin':
            return EmployeeProxy(Admin(*args))

class Employee(metaclass=ABCMeta):
    """An Employee class
    """

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return "{} - {}, {}years old {}".format(self.__class__.__name__, self.name, self.age, self.gender)

class Engineer(Employee):
    """An Engineer Employee
    """
    def get_role(self):
        return "engineer"

class Accountant(Employee):
    def get_role(self):
        return "accountant"

class Admin(Employee):
    def get_role(self):
        return "administration"
