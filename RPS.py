# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


# For this challenge, you will create a program to play Rock, Paper, Scissors. 
# A program that picks at random will usually win 50% of the time. 
# To pass this challenge your program must play matches against four different bots, winning at least 60% of the games in each match.

# In the file `RPS.py` you are provided with a function called `player`. 
# The function takes an argument that is a string describing the last move of the opponent ("R", "P", or "S"). 
# The function should return a string representing the next move for it to play ("R", "P", or "S").

# A player function will receive an empty string as an argument for the first game in a match since there is no previous play.


# The file `RPS.py` shows an example function that you will need to update.
#  The example function is defined with two arguments (`player(prev_play, opponent_history = [])`). 
#  The function is never called with a second argument so that one is completely optional. 
#  The reason why the example function contains a second argument (`opponent_history = []`) is because that is the only way to save state between consecutive calls of the `player` function.
#   You only need the `opponent_history` argument if you want to keep track of the opponent_history.

# *Hint: To defeat all four opponents, your program may need to have multiple strategies that change depending on the plays of the opponent.*

from random import randint
import statistics
from statistics import mode


  
def most_common(List):
    return(mode(List))
    
def choose_uncommon_guess(common_one,play_list):
    play_list=[x for x in play_list if x != common_one ]
    return play_list[randint(0,1)]


def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    possible_plays = ["R","P","S"]
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    last_play = opponent_history[-1]
    last_4_play = opponent_history[-4:]

    
    guess = possible_plays[randint(0,2)]
    if len(opponent_history) > 2:
         last_2_play = opponent_history[-2]
         guess = choose_uncommon_guess(most_common(opponent_history),play_list=possible_plays)
         if guess == last_play:
          guess = ideal_response[guess] 


    # special code to beat abbey bot
    if len(last_4_play) > 3:
          # signifies that opponent bot throws at us counter for what we previously threw at it
         if last_4_play[3] == last_4_play[1]:
          guess = ideal_response[last_4_play[2]]    
    return guess


# S P S P