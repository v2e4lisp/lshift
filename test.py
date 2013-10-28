import unittest
from shift import arg
from random import randint

def noop(*args, **kwargs):
    return (list(args), kwargs)

def key():
    k = "key-"
    for i in range(0, randint(0, 10)):
        k += chr(randint(0, 25) + ord('a'))
    return k

def value():
    return randint(0,100)

def randargs():
    args = [ value() for i in range(0, randint(0,10)) ]
    kwargs = {}
    for i in range(0, randint(0, 10)):
        kwargs.update({key(): value()})
    return (args, kwargs)

class TestArg(unittest.TestCase):
    def test_arg(self):
        for i in range(0, 1000):
            args = []
            kwargs = {}
            fn = noop

            for i in range(0, randint(1, 3)):
                _args, _kwargs = randargs()
                args.extend(_args)
                kwargs.update(_kwargs)
                fn = fn << arg(*_args, **_kwargs)

            _args, _kwargs = randargs()
            args.extend(_args)
            kwargs = dict(kwargs, **_kwargs)
            self.assertEqual((args, kwargs), fn(*_args, **_kwargs))

if __name__ == '__main__':
    unittest.main()
