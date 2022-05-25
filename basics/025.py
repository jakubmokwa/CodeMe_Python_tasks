def check_if_contains(n):
    numbers = [1, 5, 8, 3]
    if n in numbers:
        print(f"{n} is in specified group of values")
        return True
    print(f"{n} is not in specified group of values")
    return False


check_if_contains(2)
check_if_contains("a")
check_if_contains(3)
