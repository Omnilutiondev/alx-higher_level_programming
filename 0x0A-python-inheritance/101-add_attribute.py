#!/usr/bin/python3
"""Function adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add new attribute to an object if possible.
    Args:
        obj (any): The target object.
        att (str): The attribute to add to obj.
        value (any): The value to add.
    Raises:
        TypeError: If the attribute is not added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
