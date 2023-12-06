def shortest_palindrome(s):
    if not s:
        return ""

    rev_s = s[::-1]
    for i in range(len(s) + 1):
        if s.startswith(rev_s[i:]):
            return rev_s[:i] + s

str = input("Enter the string: ")
print(shortest_palindrome(str))