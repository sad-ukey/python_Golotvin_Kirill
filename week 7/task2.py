def find_substring(s: str, words: list) -> list:
    if not s or not words:
        return []
    word_length = len(words[0])
    word_count = len(words)
    total_length = word_length * word_count
    result_indices = []

    word_map = {}
    for word in words:
        if word in word_map:
            word_map[word] += 1
        else:
            word_map[word] = 1
    for i in range(len(s) - total_length + 1):
        seen_word_map = {}
        j = 0
        while j < word_count:

            word_index = i + j * word_length
            word = s[word_index : word_index + word_length]

            if word not in word_map:
                break
            if word in seen_word_map:
                seen_word_map[word] += 1
            else:
                seen_word_map[word] = 1
            if seen_word_map[word] > word_map[word]:
                break
            j += 1
        if j == word_count:
            result_indices.append(i)
    return result_indices


print(find_substring("barfoothefoobarman", ["foo", "bar"]))  # Вывод: [0, 9]
print(
    find_substring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])
)  # Вывод: []
print(
    find_substring("barfoofoobarthefoobarman", ["bar", "foo", "the"])
)  # Вывод: [6, 9, 12]
