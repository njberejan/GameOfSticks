# Decide on the data structure(s) that you are going to need to use to represent the state of the game when played.
# Decide on the tasks that will be part of the game loop.
# Write test function(s) for a single task.
# Write function(s) for the task and make sure your test(s) pass.
# Repeat steps 3 and 4 until all tasks are implemented.
# Write a main() function with a game loop that uses your already tested and developed functionality in conjunction with getting user input and printing output.

from sticks import Sticks
from human_v_human import Human_v_Human

def human_or_ai():
    return input("Press 'h' to play versus a human, or 'c' to play versus the computer: ").lower()


def main():
    sticks = Sticks(20)
    turn_count = 0
    sticks_left = sticks.number_of_sticks
    print("Welcome to Game of Sticks!")
    game_mode = human_or_ai()
    print(game_mode)
    if game_mode == 'h':
        Human_v_Human.game(sticks_left, turn_count, sticks)
    elif game_mode == 'c':
        pass

    #declares there are 20 sticks
    #prompt user to choose a number of sticks between 1-3
    #returns number of sticks
    #checks for game over condition

main()
#make a dictionary of lists with the hats from which the AI will draw from.
