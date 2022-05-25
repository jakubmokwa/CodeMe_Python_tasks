def extension_print():
    text = input("Write file name -> ")
    index = text.find(".")
    print(text[(index + 1):])


extension_print()
