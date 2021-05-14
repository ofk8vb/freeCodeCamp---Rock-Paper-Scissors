# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main

# `main.py` imports the game function and bots from `RPS_game.py`.

# To test your code, play a game with the `play` function. The `play` function takes four arguments:
# - two players to play against each other (the players are actually functions)
# - the number of games to play in the match
# - an optional argument to see a log of each game. Set it to `True` to see these messages.

# ```py
# play(player1, player2, num_games[, verbose])
# ```
# For example, here is how you would call the function if you want `player` and `quincy` to play 1000 games against each other and you want to see the results of each game:
# ```py
# play(player, quincy, 1000, verbose=True)
# ```

# Click the "run" button and `main.py` will run.

play(player, quincy, 1000)
play(player, abbey, 1000)
play(player, kris, 1000)
play(player, mrugesh, 1000)

# Uncomment line below to play interactively against a bot:
# play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)



# Uncomment line below to run unit tests automatically
# main(module='test_module', exit=False)