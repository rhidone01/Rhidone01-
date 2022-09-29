print('BASIC CALCULATOR')
Calculate = ''
while Calculate != 'n':
    num_1 = int(input())
    operator = input('')
    num_2 = int(input())
    result = ''
    if operator == '+':
        result = num_1 + num_2
    elif operator == '-':
        result = num_1 - num_2
    elif operator == '*':
        result = num_1 * num_2
    elif operator == '/':
        result = num_1 / num_2
    else:
        print('Invalid Operator')
    print(f'= {result}')
    Calculate = input('Calculate y/n:\n')
print('OFF')