def length_of_last_word(s):
    words = s.split()
    return len(words[-1])

s = input()
print(length_of_last_word(s))