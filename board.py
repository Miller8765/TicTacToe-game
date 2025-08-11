# File: board.py
# This module defines the Board class.

class Board:
    """
    Represents the 3x3 game board.
    It handles making moves, checking for a winner, and checking for a draw.
    """
    def __init__(self):
        # Initialize a 3x3 grid with empty spaces
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        """
        Prints the current state of the board to the console.
        """
        print("\n  0   1   2")
        print("  -----------")
        for i, row in enumerate(self.grid):
            print(f"{i} | {' | '.join(row)} |")
            print("  -----------")

    def make_move(self, row, col, symbol):
        """
        Places a player's symbol on the board at the specified row and column.
        """
        if self.grid[row][col] == ' ':
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self, symbol):
        """
        Checks if the given symbol has won the game.
        This method checks for horizontal, vertical, and diagonal wins.
        """
        # Check rows for a win
        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True

        # Check columns for a win
        for col in range(3):
            if all(self.grid[row][col] == symbol for row in range(3)):
                return True

        # Check diagonals for a win
        if (self.grid[0][0] == symbol and self.grid[1][1] == symbol and self.grid[2][2] == symbol) or \
           (self.grid[0][2] == symbol and self.grid[1][1] == symbol and self.grid[2][0] == symbol):
            return True
        
        return False

    def is_full(self):
        """
        Checks if the board is completely filled, indicating a draw.
        """
        for row in self.grid:
            if ' ' in row:
                return False
        return True