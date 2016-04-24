# Game of Sticks

This repository is for the Game of Sticks homework assignment from The Iron Yard in Durham, NC.

The assignment was to build the game "pick-up-sticks" with two functionalities: a mode wherein two human players can play head to head, and a mode whereby a human player can play against a computer opponent. In this game, two players take turns picking up between 1 and 3 sticks each turn. Whoever picks up the last stick at the end of the game (whoever's turn it is when there is one stick remaining) loses the game. The computer AI does not "learn" from game to game, and will pick a random number between 1 and 3 to determine how many sticks to pick up, until the number of sticks left is less than 4. At this point, the computer will pick the correct number of sticks to win the game.

There are multiple files because each class object exists in a separate module. Please run GameOfSticks.py to play the game.

Enjoy!
