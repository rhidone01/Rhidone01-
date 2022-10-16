import random as rd
print('GUESS GAME')
play_again = ''
while play_again != 'n':
    guess = 0
    low = 1
    high = int(input('Numbers to guess from should be from 1-: '))
    random_number = rd.randint(low,high)
    lives = 5
    while guess != random_number and lives != 0:
        random_number = int(input(f"Guess a number from 1-{high}: "))

        if guess > random_number:
            print('Guess too high! Guess again' )
            high = guess-1
            lives = lives - 1
        elif guess < random_number:
            print('Guess too low! Guess again' )
            low = guess+1
            lives = lives - 1

    if lives == 0:
        print("Sorry you've run out of lives")  
    else:
        print(f'Yay! You guesses the number {guess} correctly.') 

    play_again =input('Do you want to play GUESS GAME again y/n?: ')
print('BYE')      