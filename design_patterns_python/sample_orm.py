
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
            else:
                print(k, v)
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings    # 保存属性和列的映射关系
        attrs['__table__'] = name           # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)



class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        """重写这个取值的方法，因为不然就是self.key 这样取值了，实际上并没有这个属性"""
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    """
    子类可以隐式的继承父类的metaclass
    类名User 对应 name
    父类中的 dict 作为 基类
    这些键值对会作为metaclass魔术方法的attrs参数传过去
    """
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('aaa')
    def aaaa(self):
        pass

# 创建一个实例：
# 传入的参数调用的是dict类的__call__方法,相当于User可以当成dict使用
u = User(id=12345, name='Miku', email='test@orm.org', password='my-pwd')

# 保存到数据库：
u.save()