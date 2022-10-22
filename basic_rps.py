import random as rd
print('WELCOME TO ROCK,PAPER,SCISSORS')

def play(): 
    play_again = ''

    while play_again != 'n': 
        a = input('Rock(r),Paper(p) or Scissors(s)?: ')
        b = rd.choice(['r','p','s'])
        
        if a == b:  
            print ('It\'s a Tie')
            continue       
        elif a != 'r' and a != 'p' and a != 's':
            print('Invalid character!')
            continue  
        elif win(a,b):
            print(f'Computer chose {b},You Won!')
        elif win(b,a):  
            print(f'Computer chose {b}, You Lost!')
            
        play_again = input('To play again press "y" then enter, if not press "n" :')

def win(a,b):
            if (a == 's' and b == 'p') or (a == 'p' and b == 'r') or (a == 'r' and b == 's'):
                return True     

play()
print('BYE')    