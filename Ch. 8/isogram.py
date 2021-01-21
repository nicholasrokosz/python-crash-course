def is_isogram(string):
    return len(string) == len(set(string.lower()))

test = is_isogram('isogram')
print(test)
