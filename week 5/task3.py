from collections import defaultdict


def group_anagrams(strs):
    anagrams = defaultdict(list)

    for string in strs:
        key = "".join(sorted(string))
        anagrams[key].append(string)
    return list(anagrams.values())


# Примеры

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print(group_anagrams([""]))

print(group_anagrams(["a"]))
