# -*- coding: utf-8 -*-

""" A dict class with that allows dot accessor.  Useful for simple classes with variable attributes.
    All standard dict operations will work on a DotDict.

    Usage:
        m = DotDict()
        m = DotDict({'foo': 1, 'bar': 2})
        m.foo = 1
"""


class DotDict(dict):
    def __getattr__(self, attr):
        return self.__getitem__(attr)

    def __setattr__(self, attr, value):
        self.__setitem__(attr, value)

    def __delattr__(self, attr):
        self.__delitem__(attr)

if __name__ == "__main__":
    m = DotDict(p1=1, p2=2, pa="a", pb="b")  # standard creation
    assert m.p1 == 1
    assert m.p2 == 2
    assert m.pa == 'a'
    assert m.pb == 'b'
    
    m = DotDict({'foo': 1, 'bar': 2})  # creation from dict
    assert m.foo == 1
    assert m.bar == 2
    print('tests passed.')

    # test setting
    m.foo = "foo"
    assert m.foo == 'foo'
    m.bar = 'bar'

    # test get()
    for k in ['foo', 'bar']:
        assert m.get(k) == k

    # test del
    del m.foo
    assert m == {'bar': 'bar'}