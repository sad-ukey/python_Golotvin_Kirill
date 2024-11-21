from collections import Counter, defaultdict


def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""
    dict_t = Counter(t)
    required = len(dict_t)

    l, r = 0, 0
    formed = 0
    window_counts = defaultdict(int)

    min_len = float("inf")
    min_left = 0

    while r < len(s):
        character = s[r]
        window_counts[character] += 1

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        while l <= r and formed == required:
            character = s[l]

            if r - l + 1 < min_len:
                min_len = r - l + 1
                min_left = l
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1
        r += 1
    return "" if min_len == float("inf") else s[min_left : min_left + min_len]


print(min_window("ADOBECODEBANC", "ABC"))  # Вывод: "BANC"
print(min_window("a", "a"))  # Вывод: "a"
print(min_window("a", "aa"))  # Вывод: ""
