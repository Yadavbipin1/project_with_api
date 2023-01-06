print('hi,this is a cup game where you guess \n the cup position of cup to win rs 100 ')
print('positioning start from 0-3')
print('type \n y to play \n any text key to exit')
### one # is try and expimental block of code ------.> only help form internet is for about the random module
### and it was the first time i came to know about it

#test = [1,2,3,4,5,6,7,8,9]

test = ['empty', 'empty', '100', 'empty']
from random import shuffle

def suffled(a):
    shuffle(a)
    return a

c = input('do want to play: ')
#t = int(t)
new_list = suffled(test)
#print(new_list)
#print(new_list[t])
#c = input('enter your choice: ')

#print(new_list.index(c))
  
while  c == 'y':
    g = input('guess the position: ')
    
    if g in ['0','1','2','3']:
        g = int(g)
        if new_list[g] == '100':
            print("you won the cash prize")
        else:
            print(f"the prize is on {new_list.index('100')}")  
    else:
        print('choose correct position from 0 1 2 3 ')
    c = input('do yo wa to continue: ')
    new_list = suffled(test)
