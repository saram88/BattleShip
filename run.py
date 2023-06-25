
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
        while len(self.ships) < self.num_ships:
            row = self.get_random()
            col = self.get_random()
            if not (row, col) in self.ships:
                self.ships.append((row, col))

    def print_board(self):
        print("{}'s board".format(self.name))
        for row in self.board:
            print(" ".join(row))


def is_valid(size, value):
    if value.isnumeric():
        if (int(value) < 0) or (int(value) >= size):
            print("Invalid value")
            return False
        else:
            return True
    else:
        return False


def play(player, computer):
    print("Let's play")
    player.print_board()
    computer.print_board()

    while (len(computer.ships) > 0) and (len(player.ships) > 0):
        """Players turn"""
        guess_row = ""
        guess_col = ""

        while not is_valid(computer.size, guess_row):
            guess_row = (input("Guess row (0 - {}): ".format(player.size - 1)))
        while not is_valid(computer.size, guess_col):
            guess_col = (input("Guess col (0 - {}): ".format(player.size - 1)))

        iRow = (int)(guess_row)
        iCol = (int)(guess_col)

        if (iRow, iCol) in computer.ships:
            print("You hit a battleship!")
            computer.board[iRow][iCol] = "X"
            computer.ships.remove((iRow, iCol))
            if len(computer.ships) == 0:
                print("Congratulations! You sank all battleship!")
                break
        else:
            print("You missed the battleship!")
            computer.board[iRow][iCol] = "-"

        """Computers turn"""
        iRow = computer.get_random()
        iCol = computer.get_random()

        print("Computer guessed ({0}, {1})".format(iRow, iCol))

        if (iRow, iCol) in player.ships:
            print("Computer hit a battleship!")
            player.board[iRow][iCol] = "X"
            player.ships.remove((iRow, iCol))
            if len(player.ships) == 0:
                print("You lose! Computer sank all your battleship!")
                break
        else:
            print("Computer missed the battleship!")
            player.board[iRow][iCol] = "-"

        player.print_board()
        computer.print_board()

    print("Game Over!")


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
