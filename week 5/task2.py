def int_to_roman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman_numeral = ""

    for value, symbol in zip(values, symbols):
        while num >= value:
            roman_numeral += symbol
            num -= value
    return roman_numeral


# Примеры

print(int_to_roman(3749))
print(int_to_roman(58))
print(int_to_roman(1994))
