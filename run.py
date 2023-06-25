
from random import randint


class BattleShipBoard:
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.board = [["." for x in range(size)] for y in range(size)]
        self.guesses = []
        self.ship = []

    def get_random(self):
        return randint(0, self.size - 1)

    def setup_board(self):
        for _ in range(self.num_ships):
            row = self.get_random()
            col = self.get_random()
            self.ship.append((row, col))

    def print_board(self):
        for row in self.board:
            print(" ".join(row))


def new_game():
    size = 5
    ships = 3
    print("Welcome")
    name = input("Enter players name:\n")

    player_board = BattleShipBoard(size, ships, name, type="player")
    computer_board = BattleShipBoard(size, ships, name, type="computer")

    player_board.setup_board()
    computer_board.setup_board()

    player_board.print_board()


new_game()
