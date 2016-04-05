from sticks import Sticks
class Human_v_Human():
    def __init__(self, players):
        self.human_players = players

    def game(sticks_left, turn_count, sticks):
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
