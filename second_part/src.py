from email.headerregistry import HeaderRegistry
from hashlib import new
from random import randint
from re import X


def random_gen():
    x = 0
    while x != 15:
        x = randint(10, 20)



def decorator_to_str(func):
    # todo exercise 2
    return func


@decorator_to_str
def add(a, b):
    return str(a + b)


@decorator_to_str
def get_info(d):
    return str(d['info'])


def ignore_exception(exception):
    # todo exercise 3
    return lambda x: x


@ignore_exception(ZeroDivisionError)
def div(a, b):
    return a / b


@ignore_exception(TypeError)
def raise_something(exception):
    return None


def hellowolrd(z): 
    return 'hellowolrd' + z
# exercise 4
class CacheDecorator:
    """Saves the results of a function according to its parameters"""
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap


def test_init():
    newobj = CacheDecorator()
    assert newobj.cache == {}, "the object isn't instantiated"
    return newobj

def test_call(): 
    objet = test_init()
    objet.__call__(hellowolrd(" aurelien"))
    assert objet.cache != {}, "the cache wasn't filled"

test_call()



class MetaInherList(type):
    # todo exercise 5
    pass


class Ex:
    x = 4


class ForceToList(Ex, metaclass=MetaInherList):
    pass

