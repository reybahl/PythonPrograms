def is_permutation(w1, w2):
    w1 = sorted(w1)
    w2 = sorted(w2)
    return w1 == w2
             
print(is_permutation("test", "stet"))
