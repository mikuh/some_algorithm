from abc import ABCMeta, abstractmethod

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


class EmployeeFactory(object):
    """An employee factory class
    """
    @classmethod
    def create(cls, name, *args):
        name = name.lower().strip()
        if name == 'engineer':
            return Engineer(*args)
        elif name == 'account':
            return Accountant(*args)
        elif name == "admin":
            return Admin(*args)

