import random as rd
print('ROCK,PAPER,SCISSORS')

def play():
    play_again = ''
    while play_again != 'n':
        a = input('Rock(r),Paper(p) or Scissors(s)?: ')
        b = rd.choice(['r','p','s'])
        
        if a == b:  
            print ('It\'s a Tie')
            continue       
        elif win(a,b):
            print(f'Computer chose {b},You Won!')
        elif win(b,a):  
            print(f'Computer chose {b}, You Lost!')
        else:    
            return('Invalid')
        play_again = input('To play again press "y" then enter, if not press "n".\n')    
def win(a,b):
        if (a == 's' and b == 'p') or (a == 'p' and b == 'r') or (a == 'r' and b == 's'):
            return True  

play()
print('BYE')    