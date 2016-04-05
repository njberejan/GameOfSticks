# Decide on the data structure(s) that you are going to need to use to represent the state of the game when played.
# Decide on the tasks that will be part of the game loop.
# Write test function(s) for a single task.
# Write function(s) for the task and make sure your test(s) pass.
# Repeat steps 3 and 4 until all tasks are implemented.
# Write a main() function with a game loop that uses your already tested and developed functionality in conjunction with getting user input and printing output.
import inspect
class Sticks():
    def __init__(self, number_of_sticks):
        self.number_of_sticks = number_of_sticks

    def __sub__(self, number):
        return self.number_of_sticks - number

    def game_over(self, sticks_left):
        if sticks_left < 1:
            return True

    def player_one_turn(self):
        while True:
            number = input("Player one, pick up 1-3 sticks: ")
            if not number.isnumeric():
                print("That is not a number!")
                continue
            elif int(number) > 3:
                print("Please pick between 1 and 3!")
                continue
            else:
                return int(number)
                break

    def player_two_turn(self):
        while True:
            number = input("Player two, pick up 1-3 sticks: ")
            if not number.isnumeric():
                print("That is not a number!")
                continue
            elif int(number) > 3:
                print("Please pick between 1 and 3!")
                continue
            else:
                return int(number)
                break

class human_v_human():
    def __init__(self, players):
        self.human_players = players

    def game():
        while True:
            if sticks.game_over(sticks_left):
                print("The game is over.")
                break
            elif sticks_left == 1:
                print("You have no choice but to take the remaining stick. You have lost.")
                break
            elif turn_count % 2 == 0:
                print("There are {} sticks remaining.".format(sticks_left))
                player_one_choice = sticks.player_one_turn()
                sticks_left = sticks_left - player_one_choice
                print(sticks_left)
                turn_count += 1
                continue
            elif turn_count % 2 == 1:
                print("There are {} sticks remaining.".format(sticks_left))
                player_two_choice = sticks.player_two_turn()
                sticks_left = sticks_left - player_two_choice
                print(sticks_left)
                turn_count += 1
                continue
            else:
                print("There are {} sticks remaining.".format(sticks_left))
                player_one_choice = sticks.player_one_turn()
                sticks_left = sticks_left - player_one_choice
                print(sticks_left)
                turn_count += 1
                continue


def human_or_ai():
    return input("Press 'h' to play versus a human, or 'c' to play versus the computer: ").lower()


def main():
    from dumpfile import human_v_human
    sticks = Sticks(20)
    turn_count = 0
    sticks_left = sticks.number_of_sticks
    print("Welcome to Game of Sticks!")
    game_mode = human_or_ai()
    print(game_mode)
    if game_mode == 'h':
        human_v_human.game()
    elif game_mode == 'c':
        pass

    #declares there are 20 sticks
    #prompt user to choose a number of sticks between 1-3
    #returns number of sticks
    #checks for game over condition
main()
