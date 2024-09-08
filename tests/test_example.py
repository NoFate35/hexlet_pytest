from hexlet_pytest.example import Obj
import pytest


@pytest.fixture()
def items():
    return {
        'key': 'value',
        'key2': {
            'key3': 'value3'
        }
    }


def test_simple_get(items):
    obj = Obj(items)

    assert obj['key'] == 'value'
    assert obj.key == 'value'


def test_nested_get(items):
    obj = Obj(items)

    assert obj['key2']['key3'] == 'value3'
    assert obj.key2.key3 == 'value3'
    assert obj['key2'].key3 == 'value3'


def test_none_key(items):
    obj = Obj(items)

    assert obj['foo'] is None
    assert obj.foo is None


def test_simple_set(items):
    obj = Obj(items)

    obj.key = 'new value'
    assert obj['key'] == 'new value'
    assert obj.key == 'new value'


def test_nested_set(items):
    obj = Obj(items)

    obj.key2.key3 = 'new value'
    assert obj['key2']['key3'] == 'new value'
    assert obj.key2.key3 == 'new value'

    
