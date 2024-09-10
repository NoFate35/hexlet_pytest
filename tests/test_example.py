from hexlet_pytest.example import Proxy
import pytest


class sourceObject:
    def __init__(self, attrs):
        for key, value in attrs.items():
            self.__setattr__(key, value)

    def foo(self):
        return 'foobar'

    def wrong_foo(self):
        raise Exception('method with error')


def test_existing_properties():
    d = {'key': 42}
    source_obj = sourceObject(d)
    proxy = Proxy(source_obj)

    assert proxy.foo() == source_obj.foo()
    assert proxy.key == source_obj.key


def test_set_attributes():
    d = {'key': 42}
    source_obj = sourceObject(d)
    proxy = Proxy(source_obj)
    proxy.key2 = 'foo'
    assert proxy.key2 == 'foo'


def test_logging():
    d = {'key': 42}
    source_obj = sourceObject(d)
    proxy = Proxy(source_obj)

    # make some calls
    proxy.key
    proxy.foo()

    assert len(proxy.get_log()) == 2


def test_errors_logging():
    d = {'key': 'value'}
    source_obj = sourceObject(d)
    proxy = Proxy(source_obj)

    # make some right and wrong attributes calles
    proxy.key
    proxy.foo()
    with pytest.raises(Exception):
        proxy.wrong_foo(), "Proxy should reraise exceptions"

    # check logging
    assert len(proxy.get_log()) == 2
    # check errors logging
    assert len(proxy.get_errors_log()) == 1
