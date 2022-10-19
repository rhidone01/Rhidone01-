from words import word_list
import random as rd
import string
word = rd.choice(word_list)

def valid_word(word):
    while ' ' in word or '-' in word:
        word = rd.choice(word_list)
    return word.upper
def hangman():
    user_letter = input('Enter a letter: ')
    s_word = valid_word(word)
    alphabets = set(string.ascii_uppercase)
    word_letters = set(s_word)
    used_letters = ()
    print(word_letters)
hangman()