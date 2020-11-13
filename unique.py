def is_unique(word):
    """Function to find if a 
    string is unique.
    """
    vals =  [False] * 128
    for l in word:
        if vals[ord(l)]:
            return False
        else:
            vals[ord(l)] = True
    return True

print(is_unique(input("Hello!!!!!!!!"))

