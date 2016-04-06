import random
from sticks import Sticks


class Human_v_CPU():
# list_name[key] = value

    def __init__(self, players):
        self.players = players

    def cpu_turn(turn_count, cpu_dict, sticks_left):
        for turn_count in cpu_dict:
            return cpu_dict[random.randint(1, 3)]

    def game(sticks_left, turn_count, sticks, cpu_dict, cpu_hats):
        while True:
            if sticks.game_over(sticks_left):
                print("The game is over.")
                break
            elif sticks_left == 1:
                if turn_count % 2 == 0:
                    print("You have no choice but to take the remaining stick. You have lost.")
                    for key in cpu_hats:
                        cpu_dict[turn_count].append(cpu_choice)
                    print(cpu_hats)
                    break
                else:
                    print("The computer has no choice but to take the remaining stick. You win!")
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
                cpu_choice_list = Human_v_CPU.cpu_turn(turn_count, cpu_dict, sticks_left)
                # print(cpu_choice_list)
                cpu_choice = random.choice(cpu_choice_list)
                # print(cpu_choice)
                cpu_hats[turn_count] = cpu_choice
                print("The CPU picks up {} sticks.".format(cpu_choice))
                sticks_left = sticks_left - cpu_choice
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
