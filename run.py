
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


def play(player, computer):
    print("Let's play")
    player.print_board()
    computer.print_board()

    while (len(computer.ships) > 0) and (len(player.ships) > 0):
        """Players turn"""
        guess_row = int(input("Guess row (0 - {}): ".format(player.size - 1)))
        guess_col = int(input("Guess col (0 - {}): ".format(player.size - 1)))

        if (guess_row, guess_col) in computer.ships:
            print("You hit a battleship!")
            computer.board[guess_row][guess_col] = "X"
            computer.ships.remove((guess_row, guess_col))
            if len(computer.ships) == 0:
                print("Congratulations! You sank all battleship!")
                break
        else:
            print("You missed the battleship!")
            computer.board[guess_row][guess_col] = "-"

        """Computers turn"""
        guess_row = computer.get_random()
        guess_col = computer.get_random()

        print("Computer guessed ({0}, {1})".format(guess_row, guess_col))

        if (guess_row, guess_col) in player.ships:
            print("Computer hit a battleship!")
            player.board[guess_row][guess_col] = "X"
            player.ships.remove((guess_row, guess_col))
            if len(player.ships) == 0:
                print("You lose! Computer sank all your battleship!")
                break
        else:
            print("Computer missed the battleship!")
            player.board[guess_row][guess_col] = "-"

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
