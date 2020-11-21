def compress_string(text):
    compressed = ''
    previous = ''
    occurrences = 1
    i = 0
    while i < len(text):
        x = text[i]
        if x == previous:
            occurrences += 1
        elif i != 0:
            compressed += f'{previous}{occurrences}'
            occurrences = 1
        if len(text) - 1 == i:
            compressed +=  f'{text[i]}{occurrences}'
        previous = x
        i += 1
    return compressed
print(compress_string(input()))