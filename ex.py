digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']

numbers = {}
for i in range(0, len(digits)):
    numbers[digits[i]] = {
        'french': fr[i],
        'english': en[i],
    }
print(numbers)