import random

comp_options = ['rock', 'paper', 'scissors']
c = 0
h = 0
print('Human! Let`s play rock paper scissors up to three wins!')
while c < 3 and h < 3:
    comp_turn = random.choice(comp_options)
    print('Random choice of computer (for checking):', comp_turn)
    humans_turn = input('Your turn, human: ')
    if comp_turn == humans_turn:
        print('Draw!')
    elif comp_turn == 'rock' and humans_turn == 'scissors' or comp_turn == 'scissors' and humans_turn == 'paper' or comp_turn == 'paper' and humans_turn == 'rock':
        c = c + 1
    elif comp_turn == 'rock' and humans_turn == 'paper' or comp_turn == 'scissors' and humans_turn == 'rock' or comp_turn == 'paper' and humans_turn == 'scissors':
        h = h + 1
    else:
        print('Human! Enter rock, paper or scissors!')
    print('Game score: Computer:', c, 'Human:', h)
    print()
if c == 3:
    print('The computer wins!')
elif h == 3:
    print('Human wins!')