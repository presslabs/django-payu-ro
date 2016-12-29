from random import randint
import pytest

from payu.conf import MagicSingleton


class SimpleConfigurationExample(object):
    __metaclass__ = MagicSingleton

    simple_property = 'test_value'


def test_magic_singleton():
    SimpleConfigurationExample.another_property = 'another_test_value'
    assert SimpleConfigurationExample.another_property == 'another_test_value'

    assert SimpleConfigurationExample._instance
    assert SimpleConfigurationExample.simple_property == 'test_value'

    huge_int_value = randint(2**1000, 2**1001)
    SimpleConfigurationExample.simple_property = huge_int_value
    assert SimpleConfigurationExample.simple_property == huge_int_value

    class_property = SimpleConfigurationExample.simple_property
    instance_property = SimpleConfigurationExample._instance.simple_property
    assert class_property is instance_property
