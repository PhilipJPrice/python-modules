class Color:
    """
    Sets a rgb value and name to a variable defined by user
    _functions suggest private scopes but can be overridden
    ~ python -i oop_python/polygon/color.py
    >>> c = Color("#ff0000", "bright red")
    >>> print(c.name)
    bright red
    >>> c.name = "red"
    >>> print(c.name)
    red
    >>> c.name = ""
    Exception: Invalid Name
    """
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self.name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)
