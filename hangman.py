from words import word_list
import random as rd
import string

word = rd.choice(word_list)
def valid_word(word):
    while ' ' in word or '-' in word:
        word = rd.choice(word_list)
    return word.upper()
    
print('WELCOME TO HANGMAN')
play_again = ''
while play_again != 'n':
    def hangman():
        
        selected_word = valid_word(word)
        alphabets = set(string.ascii_uppercase)
        word_letters = set(selected_word)
        used_letters = set()
        lives = 5

        while len(word_letters) > 0 and lives > 0:

            print(f"You have {lives} live(s) left, and have entered {' '.join(used_letters)}")
            word_list = [letter if letter in used_letters else '-' for letter in selected_word]
            print(f"Current guess is {' '.join(word_list)}")
            user_letter = input('Guess a letter: ').upper()

            if user_letter in alphabets - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:
                    lives = lives - 1
            elif user_letter in used_letters:
                print('You have already used that letter.')
            else:
                print('You entered an invalid character.') 
        if lives == 0:
            print(f'You ran out of live the word is {word.upper()}')
        else:
            print(f'Yay! You have successfully guessed the word {word.upper()}. ')
    hangman()
    play_again = input('To play again press "y" then enter, if not press "n": ')
print('BYE')