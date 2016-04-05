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
