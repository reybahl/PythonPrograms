def permutation_of_palindrome(text):
    num_of_occurrences = [0] * 128 #List of occurrences of each ASCII value
    
    for i in text:
        num_of_occurrences[ord(i)] += 1

    odds = 0
    for occurrence in num_of_occurrences:
        if odds > 1:
            return False
        if occurrence %2 == 1:
            odds +=1

    return True

print(permutation_of_palindrome(input()))

