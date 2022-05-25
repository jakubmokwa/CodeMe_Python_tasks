def number_check(n):
    if n > 0:
        return True
    print("Number must be positive!")
    return False


def string_print(n):
    if not number_check(n):
        return
    text = input("Write your word or sentence -> ")
    if len(text) > 2:
        print(text[:2] * n)
    else:
        print(text * n)


string_print(3)
string_print(5)
