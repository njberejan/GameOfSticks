# Decide on the data structure(s) that you are going to need to use to represent the state of the game when played.
# Decide on the tasks that will be part of the game loop.
# Write test function(s) for a single task.
# Write function(s) for the task and make sure your test(s) pass.
# Repeat steps 3 and 4 until all tasks are implemented.
# Write a main() function with a game loop that uses your already tested and developed functionality in conjunction with getting user input and printing output.
from itertools import cycle
class Sticks():
    def __init__(self, number_of_sticks, sticks_left):
        self.number_of_sticks = number_of_sticks
        self.sticks_left = sticks_left

    def __sub__(self, number):
        return self.number_of_sticks - number

    def game_over(self, sticks_left):
        if sticks_left < 1:
            return True

    def player_turn(self, player):
        while True:
            number = input("{}, pick up 1-3 sticks: ".format(player))
            if not number.isnumeric():
                print("That is not a number!")
                continue
            elif int(number) > 3:
                print("Please pick between 1 and 3!")
                continue
            else:
                return int(number)
                break


    def do_turn(self, player, sticks, sticks_left):
        print("There are {} sticks remaining.".format(sticks_left))
        player_choice = sticks.player_turn(player)
        sticks_left = sticks.sticks_left - player_choice
        return sticks_left


# for player in cycle(["player1", "player2"]):
#     do_turn(player)
#     if game_over():
#         break

# def do_turn(player, sticks_left):
#     print("There are {} sticks remaining.".format(sticks_left))
#     player_choice = sticks.player_turn()
#     sticks_left = sticks_left - player_choice
#     print(sticks_left)


def main():
    player = ["player1", "player2"]
    sticks = Sticks(20, 20)
    #game begins with 20 sticks and 20 left
    sticks_left = sticks.number_of_sticks
    #variable assigned
    print("Welcome to Game of Sticks!")
    #prints greeting
    while True:
    #loops beings
        for player in cycle(["player1", "player2"]):
            #theoretically for switching players
            sticks.do_turn(player, sticks, sticks.sticks_left)
            #should execute the turn which returns player choice and subtracts from sticks left
            if sticks.game_over(sticks_left):
                print("The game is over.")
                break
            else:
                continue

    #declares there are 20 sticks
    #prompt user to choose a number of sticks between 1-3
    #returns number of sticks
    #checks for game over condition
main()

#count of turns which increases
# if modulo 2 returns 0, it's one player's turn, if modulo 2 returns 1, it's the other player's turn.
