#!/usr/bin/python3

"""defines an inherited list class MyList."""

class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """print a list in sorted ascending oreder."""
        print(sorted(self))
