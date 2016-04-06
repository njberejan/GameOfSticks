# Decide on the data structure(s) that you are going to need to use to represent the state of the game when played.
# Decide on the tasks that will be part of the game loop.
# Write test function(s) for a single task.
# Write function(s) for the task and make sure your test(s) pass.
# Repeat steps 3 and 4 until all tasks are implemented.
# Write a main() function with a game loop that uses your already tested and developed functionality in conjunction with getting user input and printing output.

from sticks import Sticks
from human_v_human import Human_v_Human
from human_v_cpu import Human_v_CPU
cpu_hats = {}
cpu_dict = {
0: [1, 2, 3],
1: [1, 2 ,3],
2: [1, 2, 3],
3: [1, 2, 3],
4: [1, 2, 3],
5: [1, 2, 3],
6: [1, 2, 3],
7: [1, 2, 3],
8: [1, 2, 3],
9: [1, 2, 3],
10: [1, 2, 3],
11: [1, 2, 3],
12: [1, 2, 3],
13: [1, 2, 3],
14: [1, 2, 3],
15: [1, 2, 3],
16: [1, 2, 3],
17: [1, 2, 3],
18: [1, 2, 3],
19: [1, 2, 3],
20: [1, 2, 3],
}
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
        Human_v_CPU.game(sticks_left, turn_count, sticks, cpu_dict, cpu_hats)
    while True:
        play_again = input("Would you like to play again? Y/n: ")
        if play_again.lower() == 'y':
            main()
        elif play_again.lower() == 'n':
            break
        else:
            print("Please enter 'y' or 'n'.")
            continue


    #declares there are 20 sticks
    #prompt user to choose a number of sticks between 1-3
    #returns number of sticks
    #checks for game over condition

main()
