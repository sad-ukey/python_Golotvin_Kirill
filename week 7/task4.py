def find_repeated_dna_sequences(s: str) -> list:
    if len(s) < 10:
        return []
    sequence_count = {}
    result = set()

    for i in range(len(s) - 9):
        substring = s[i : i + 10]
        if substring in sequence_count:
            sequence_count[substring] += 1
            result.add(substring)
        else:
            sequence_count[substring] = 1
    return list(result)


print(
    find_repeated_dna_sequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
)  # Вывод: ["AAAAACCCCC", "CCCCCAAAAA"]
print(find_repeated_dna_sequences("AAAAAAAAAAAAA"))  # Вывод: ["AAAAAAAAAA"]
