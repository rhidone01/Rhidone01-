import random as rd
print('WELCOME TO GUESS GAME (PLAYER VERSION)')
play_again = ''
while play_again != 'n':
    guess = 0
    low = 1
    high = int(input('Numbers to guess from should be from 1-: '))
    d_high = input('Please enter the number again: ')
    random_number = rd.randint(low,high)
    lives = 5
    while guess != random_number and lives != 0:
        
        guess = int(input(f"Guess a number from 1-{d_high}: "))

        if guess > high or guess == 0:
            print(f'you have entered an invalid number!\nYou have {lives} live left.')

        elif guess > random_number:
            print('Guess too high! Guess again.' )
            high = guess-1
            lives = lives - 1
            print(f'You have {lives} lives left')
        elif guess < random_number:
            print('Guess too low! Guess again' )
            low = guess+1
            lives = lives - 1
            print(f'You have {lives} lives left.')
        
    if lives == 0:
        print("Sorry you've run out of lives")  
    else:
        print(f'Yay! You guessed the number {guess} correctly.') 

    play_again =input('To play again press "y" then enter, if not press "n": ')
print('BYE')   