
from random import randint


class BattleShipBoard:
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.board = [["." for x in range(size)] for y in range(size)]
        self.guesses = []
        self.ships = []

    def get_random(self):
        return randint(0, self.size - 1)

    def setup_board(self):
        for _ in range(self.num_ships):
            row = self.get_random()
            col = self.get_random()
            self.ships.append((row, col))

    def print_board(self):
        print("{}'s board".format(self.name))
        for row in self.board:
            print(" ".join(row))


def play(player, computer):
    print("Let's play")
    player.print_board()
    computer.print_board()

    turns = 5
    for turn in range(turns):
        guess_row = int(input("Guess row (0 - {}): ".format(player.size - 1)))
        guess_col = int(input("Guess col (0 - {}): ".format(player.size - 1)))

        if (guess_row, guess_col) in computer.ships:
            print("You hit a battleship!")
            computer.board[guess_row][guess_col] = "X"
            computer.ships.Remove(guess_row, guess_col)
            if len(computer.ships) == 1:
                print("Congratulations! You sank all battleship!")
                break
        else:
            print("You missed the battleship!")
            computer.board[guess_row][guess_col] = "-"

        player.print_board()
        computer.print_board()

    print("Game Over! Players ran out of guesses.")


def new_game():
    size = 5
    ships = 3
    print("Welcome")
    name = input("Enter players name:\n")

    player_board = BattleShipBoard(size, ships, name, type="player")
    computer_board = BattleShipBoard(size, ships, "Computer", type="computer")

    player_board.setup_board()
    computer_board.setup_board()

    play(player_board, computer_board)


new_game()
