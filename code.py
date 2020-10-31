from time import time

start_time = time()

length = 10
letters = 'RLRLLRLLRR'

list_letters = [letter for letter in enumerate(letters)]
count_R = letters.count('R')
count_L = letters.count('L')

positions_L = [ number[0] for number in list_letters if number[1] == 'L']

if count_R > count_L:
    if positions_L[-1] == length-1:
        print(letters[:positions_L[-1]].replace('L','R')+letters[positions_L[-1]:])
        
    else:
        number_R1 = letters[:positions_L[-1]].count('R')
        number_R2 = letters[positions_L[-1]:].count('R')
        if number_R1 > number_R2:
            new_letters = letters[:positions_L[-1]].replace('L','R')+letters[positions_L[-1]:].replace('R','L')
            count_changes = letters[:positions_L[-1]].count('L')+letters[positions_L[-1]:].count('R')
            print(f'Количество изменений {count_changes}')
            print(new_letters)
            
elif count_R < count_L:
    pass
        
end_time = time()
print(f'Затраченное время {end_time-start_time}')
