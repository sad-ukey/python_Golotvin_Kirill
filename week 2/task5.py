def isPalindrome(s):
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1]


s = 'A man, a plan, a canal: Panama'
print(isPalindrome(s))
