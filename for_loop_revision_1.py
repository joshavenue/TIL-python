data_A = [1,2,3,6,7,8,9]
data_B = [1,2,7,8]
count = 0

for number1 in data_A:
    for number2 in data_B:
        if number1 == number2:
            print('{} is also appeared in {}'.format(number1,number2))
            count += 1
    else:
        pass

print('There are only {} matching numbers between Data A and Data B.'.format(count))
