from time import time

start_time = time()

length = 8
letters = 'LLRLLLRL'

list_letters = [letter for letter in enumerate(letters)]
count_R = letters.count('R')
count_L = letters.count('L')

positions_L = [ number[0] for number in list_letters if number[1] == 'L']
positions_R = [ number[0] for number in list_letters if number[1] == 'R']

if count_R > count_L:
    if positions_L[-1] == length-1:
        print(letters[:positions_L[-1]].replace('L','R')+letters[positions_L[-1]:])
        
    elif positions_L[-1] == 0:
        print(letters[positions_L[-1]:].replace('L','R'))
        
    else:
        number_R1 = letters[:positions_L[-1]].count('R')
        number_R2 = letters[positions_L[-1]:].count('R')
        if number_R1 > number_R2:
            new_letters = letters[:positions_L[-1]].replace('L','R')+letters[positions_L[-1]:].replace('R','L')
            print(f'Входные данные {letters}')
            print(f'Выходные данные {new_letters}')
            
elif count_R < count_L:
    if positions_R[-1] == length-1:
        print(letters[:positions_R[-1]].replace('R','L')+letters[positions_R[-1]:])
        
    elif positions_R[-1] == 0:
        print(letters[positions_R[-1]:].replace('R','L'))
        
    else:
        number_L1 = letters[:positions_R[-1]].count('L')
        number_L2 = letters[positions_R[-1]:].count('L')
        if number_L1 > number_L2:
            new_letters = letters[:positions_R[-1]].replace('L','R')+letters[positions_R[-1]:].replace('R','L')
            print(f'Входные данные {letters}')
            print(f'Выходные данные {new_letters}')
        
end_time = time()
print(f'Затраченное время {end_time-start_time}')
