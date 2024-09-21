s = input()

left = 0
right = 0
char_index = {}
max_len = 0

while right < len(s):
    if s[right] in char_index:
        left = max(left, char_index[s[right]] + 1)
    char_index[s[right]] = right
    max_len = max(max_len, right - left + 1)
    right += 1

print(max_len)
