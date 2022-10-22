import random as rd
print('WELCOME TO GUESS GAME (COMPUTER VERSION)')
play_again = ''
while play_again != 'n':
    guess_range = int(input('The Computer should guess a number from 1-: '))
    low = 1
    high = guess_range
    computer_guess = rd.randint(1,guess_range)
    feedback = ''
    lives = 5

    while feedback != 'c' and lives != 0 and low < high:
        
        feedback = input(f'Is {computer_guess} too high(h), too low(l) or correct(c)?: ')
        
        if feedback == 'h':
            lives = lives - 1
            high = computer_guess - 1
            computer_guess = rd.randint(low,high)
        elif feedback == 'l':
            lives = lives - 1
            low = computer_guess + 1
            computer_guess = rd.randint(low,high)
        else:
            print('You have entered an invalid character!')
    if feedback == 'c':
        print(f'Yay! Computer guessed the number {computer_guess} correctly.')
    elif lives == 0:
        print('Computer ran out of lives!')
    else:
        fb = input(f'Is {low} too high(h), too low(l) or correct(c)?: ')
        if fb == 'c':
            print(f'Yay! Computer guessed the number {low} correctly.')
        else:
            print(f'Based on the feedbacks provided the number is {low}')
    play_again = input('To play again press "y" then enter, if not press "n": ')
print('BYE')