def func(haystack, needle):
    
    if len(haystack) < len(needle):
        return -1
    
    for i, j in zip(range(0, len(haystack)-len(needle)+1), range(len(needle)-1, len(haystack))):
        if haystack[i:j+1] == needle:
            return i
    
    return -1

haystack = input()
needle = input()

print(func(haystack, needle))