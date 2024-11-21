def findRepeatedDnaSequences(s: str):
    if len(s) < 10:
        return []
    seen = set()
    repeated = set()

    for i in range(len(s) - 9):
        substring = s[i : i + 10]
        if substring in seen:
            repeated.add(substring)
        else:
            seen.add(substring)
    return list(repeated)


print(
    findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
)  # Вывод: ["AAAAACCCCC", "CCCCCAAAAA"]
print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))  # Вывод: ["AAAAAAAAAA"]
