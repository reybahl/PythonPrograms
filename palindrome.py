def is_palindrome(text):
    x = 0
    while x < round(len(text)/2, 0):
        if text[x] != text[(len(text) -1) - x]:
            return False
        x += 1

    return True

print(is_palindrome(input()))
