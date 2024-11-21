from collections import Counter, defaultdict


def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""
    required = Counter(t)

    formed = defaultdict(int)

    left, right = 0, 0
    have, need = 0, len(required)
    min_length = float("inf")
    min_window_start = 0

    while right < len(s):
        char = s[right]
        formed[char] += 1

        if char in required and formed[char] == required[char]:
            have += 1
        while have == need:

            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window_start = left
            char = s[left]
            formed[char] -= 1
            if char in required and formed[char] < required[char]:
                have -= 1
            left += 1
        right += 1
    return (
        ""
        if min_length == float("inf")
        else s[min_window_start : min_window_start + min_length]
    )


print(min_window("ADOBECODEBANC", "ABC"))  # Вывод: "BANC"
print(min_window("a", "a"))  # Вывод: "a"
print(min_window("a", "aa"))  # Вывод: ""
