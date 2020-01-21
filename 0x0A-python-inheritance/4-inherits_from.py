#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ returns False if the object is directly a instance of a clase
    True in other case
    """
    return False if type(obj) == a_class else isinstance(obj, a_class)
