import random as rd
a = int(input('The Computer should guess a number from 1-: '))
low = 1
high = a
computer_guess = rd.randint(1,a)
c = ''
lives = 5

while c != 'c' and lives != 0:
    c = input(f'Is {computer_guess} too high(h), too low(l) or correct(c)?: ')
    if c == 'h':
        lives = lives - 1
        high = computer_guess - 1
        computer_guess = rd.randint(low,high)
    elif c == 'l':
        lives = lives - 1
        low = computer_guess + 1
        computer_guess = rd.randint(low,high)

if c == 'c':
    print(f'Yay! Computer guessed the number {computer_guess} correctly.')
elif lives == 0:
    print('Computer ran out of lives!')