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
    Calculate = input(' To alculate press "y" then enter, if not press "n": ')
print('BYE')