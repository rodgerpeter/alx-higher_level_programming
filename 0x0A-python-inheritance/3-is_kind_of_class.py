#!/usr/bin/python3

"""Define a class and inherited class-checking function."""

def is_kind_of_class(obj, a_class):

    if isinstances(obj,a_class):
        return True
    return False 
