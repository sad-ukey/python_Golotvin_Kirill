from collections import Counter


def findSubstring(s: str, words: list) -> list:
    if not s or not words:
        return []
    word_length = len(words[0])
    word_count = len(words)
    total_length = word_length * word_count
    word_map = Counter(words)
    indices = []

    for i in range(len(s) - total_length + 1):
        substring = s[i: i + total_length]
        seen_words = Counter()

        for j in range(0, total_length, word_length):
            word = substring[j: j + word_length]
            if word in word_map:
                seen_words[word] += 1

                if seen_words[word] > word_map[word]:
                    break
            else:
                break
        if seen_words == word_map:
            indices.append(i)
    return indices


print(findSubstring("barfoothefoobarman", ["foo", "bar"]))  # Вывод: [0, 9]
print(
    findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])
)  # Вывод: []
print(
    findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"])
)  # Вывод: [6, 9, 12]
