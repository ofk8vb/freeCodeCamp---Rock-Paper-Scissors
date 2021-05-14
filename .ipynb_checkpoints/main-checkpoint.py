{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'RPS_game'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-843e1db64292>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# This entrypoint file to be used in development. Start by reading README.md\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mRPS_game\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mplay\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmrugesh\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mabbey\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mquincy\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkris\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mhuman\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrandom_player\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mRPS\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mplayer\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0munittest\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mmain\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'RPS_game'"
     ]
    }
   ],
   "source": [
    "# This entrypoint file to be used in development. Start by reading README.md\n",
    "from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player\n",
    "from RPS import player\n",
    "from unittest import main\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "play(player, quincy, 1000)\n",
    "play(player, abbey, 1000)\n",
    "play(player, kris, 1000)\n",
    "play(player, mrugesh, 1000)\n",
    "\n",
    "# Uncomment line below to play interactively against a bot:\n",
    "# play(human, abbey, 20, verbose=True)\n",
    "\n",
    "# Uncomment line below to play against a bot that plays randomly:\n",
    "# play(human, random_player, 1000)\n",
    "\n",
    "\n",
    "\n",
    "# Uncomment line below to run unit tests automatically\n",
    "# main(module='test_module', exit=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# main.py imports the game function and bots from RPS_game.py.\n",
    "\n",
    "# To test your code, play a game with the play function. The play function takes four arguments:\n",
    "\n",
    "# two players to play against each other (the players are actually functions)\n",
    "# the number of games to play in the match\n",
    "# an optional argument to see a log of each game. Set it to True to see these messages.\n",
    "# play(player1, player2, num_games[, verbose])\n",
    "# play(player1, player2, num_games[, verbose])\n",
    "# For example, here is how you would call the function if you want player and quincy to play 1000 games against each other \n",
    "# and you want to see the results of each game:\n",
    "\n",
    "# play(player, quincy, 1000, verbose=True)\n",
    "# play(player, quincy, 1000, verbose=True)\n",
    "# Click the \"run\" button and main.py will run."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
