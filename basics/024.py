def vowel_check(char):
    if not str(char).isalpha():
        print(f"{char} is not a letter")
        return
    if len(char) > 1:
        print(f"{char} is not a single letter")
        return
    tmp_char = char.lower()
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
    polish_vowels = ['ą', 'ę', 'ó']
    if tmp_char in vowel_list or polish_vowels:
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")


vowel_check('a')
vowel_check('b')
vowel_check(1)
vowel_check("ab")
