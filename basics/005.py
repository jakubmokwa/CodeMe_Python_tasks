def name_surname():
    text = input("Write your name and surname -> ")
    tmp_list = text.split()
    print(tmp_list[::-1])


name_surname()
