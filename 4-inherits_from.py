#!usr/bin/python3
"""subclass checker"""


def inherits_from(obj, a_class):
    """returns sublass yes"""
    if type(obj) == a_class:
        return false
    return issubclass(type(obj), a_class)
