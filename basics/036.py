def add_objects(obj1, obj2):
    if type(obj1) == type(obj2) == int:
        return obj1 + obj2
    else:
        return False


print(add_objects('a', 1))
print(add_objects(1, 2))
print(add_objects(2.0, 4))
