#Functions, dictionaries 
import random

def get_choices():
    player_choice = input('Enter a choice rock, paper, scissors: ')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {'player': player_choice, 'computer': computer_choice}
    return choices

def check_win(player, computer):
    print(f'You chose  {player}, computer chose {computer}')
    if player == computer:
        return('Tie')   
     
    elif player == 'rock':
        if computer == 'scissors':
            return ('Player has won, rock wins with scissors')
        else:
            return 'Computer won, paper covers rock'
    
    elif player == 'paper':
        if computer == 'rock':
            return ('Player has won, paper wins with rock')
        else:
            return 'Computer won, scissors cut paper'
    
    elif player == 'scissors':
        if computer == 'paper':
            return ('Player has won, scissors cut paper')
        else:
            return 'Computer won, rock wins with scissors'
    
choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)