def funny_division(divider):
    try:
        return 100 / divider
    except ZeroDivisionError:
        return "Zero is not a good idea!"
    except TypeError:
        return "Numbers only!"

print(funny_division(0))
print(funny_division(50.0))
print(funny_division("hello"))
