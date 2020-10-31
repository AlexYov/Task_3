from timeit import default_timer

start_time = default_timer()

length = 10
letters = 'LLRRLRRRRL'

list_letters = [letter for letter in enumerate(letters)]
count_R = letters.count('R')
count_L = letters.count('L')

positions_L = [ number[0] for number in list_letters if number[1] == 'L']
positions_R = [ number[0] for number in list_letters if number[1] == 'R']

if count_R > count_L:
    if positions_L[-1] == length-1:
        new_letters = letters[:positions_L[-1]].replace('L','R')+letters[positions_L[-1]:]
        print(f'Входные данные {letters}')
        print(f'Выходные данные {new_letters}')
        
    elif positions_L[-1] == 0:
        new_letters = letters[positions_L[-1]:].replace('L','R')
        print(f'Входные данные {letters}')
        print(f'Выходные данные {new_letters}')
        
    else:
        number_R1 = letters[:positions_L[-1]].count('R')
        number_R2 = letters[positions_L[-1]:].count('R')
        new_letters = letters[:positions_L[-1]].replace('L','R')+letters[positions_L[-1]:].replace('R','L')
        print(f'Входные данные {letters}')
        print(f'Выходные данные {new_letters}')
        
        
            
elif count_R < count_L:
    if positions_R[-1] == length-1:
        new_letters = letters[:positions_R[-1]].replace('R','L')+letters[positions_R[-1]:]
        print(f'Входные данные {letters}')
        print(f'Выходные данные {new_letters}')
        
    elif positions_R[-1] == 0:
        new_letters = letters[positions_R[-1]:].replace('R','L')
        print(f'Входные данные {letters}')
        print(f'Выходные данные {new_letters}')
        
    else:
        number_L1 = letters[:positions_R[-1]].count('L')
        number_L2 = letters[positions_R[-1]:].count('L')
        new_letters = letters[:positions_R[-1]].replace('L','R')+letters[positions_R[-1]:].replace('R','L')
        print(f'Входные данные {letters}')
        print(f'Выходные данные {new_letters}')
        
end_time = default_timer()
print(f'Затраченное время {end_time-start_time}')
