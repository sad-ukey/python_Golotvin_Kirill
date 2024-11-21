def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    max_length = 0
    start = 0

    for index, char in enumerate(s):

        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = index
        max_length = max(max_length, index - start + 1)
    return max_length


print(length_of_longest_substring("abcabcbb"))  # Вывод: 3
print(length_of_longest_substring("bbbbb"))  # Вывод: 1
print(length_of_longest_substring("pwwkew"))  # Вывод: 3
