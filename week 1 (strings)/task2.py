def ifPolindromic(s):
    for i, j in zip(range(len(s) // 2), range(1, (len(s) // 2) + 1)):
        if s[i] != s[-j]:
            return ''
    return s


longestPolindrome = ''
s = input()
srez = 1

for i in range(len(s)):
    for j in range(srez, len(s)):
        if s[i] == s[j]:
            polindrome = ifPolindromic(s[i:j+1])
            if len(longestPolindrome) < len(polindrome):
                longestPolindrome = polindrome
    srez += 1
    
print(longestPolindrome)        

