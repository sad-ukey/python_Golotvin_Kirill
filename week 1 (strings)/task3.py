numbers =  {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
           }

digits = input()
letter_list = list(digits)
srez = 1
final_list = []

for i in range(len(letter_list)):
    int_i = int(letter_list[i])
    str_i = letter_list[i]
    for j in range(srez, len(letter_list)):
        int_j = int(letter_list[j])
        str_j = letter_list[j]
        print(i, '', j, int_i, '', int_j)
        #for ii in numbers
        #final_list.append(numbers[i]+)
        
    srez += 1
