# File: main.py
# This is the main application file that runs the Tic-Tac-Toe game.

# Import the necessary classes from their respective modules.
# The `from .` syntax ensures a relative import from the current package.
from player import Player
from board import Board

class Game:
    """
    Manages the overall game flow, player turns, and game state.
    """
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player_index = 0

    def get_current_player(self):
        """
        Returns the player whose turn it is.
        """
        return self.players[self.current_player_index]

    def switch_player(self):
        """
        Switches the current player for the next turn.
        """
        self.current_player_index = (self.current_player_index + 1) % 2

    def play(self):
        """
        The main game loop.
        """
        print("Welcome to Tic-Tac-Toe!")
        winner = None

        while not winner:
            current_player = self.get_current_player()
            self.board.display()
            print(f"It's {current_player.name}'s turn ({current_player.symbol}).")

            # Get and validate the player's move
            while True:
                try:
                    row = int(input("Enter row (0, 1, or 2): "))
                    col = int(input("Enter column (0, 1, or 2): "))
                    if 0 <= row <= 2 and 0 <= col <= 2:
                        if self.board.make_move(row, col, current_player.symbol):
                            break
                        else:
                            print("That spot is already taken. Try again.")
                    else:
                        print("Invalid input. Please enter numbers between 0 and 2.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            # Check for a winner or a draw
            if self.board.check_winner(current_player.symbol):
                winner = current_player
                self.board.display()
                print(f"Congratulations, {winner.name} wins!")
            elif self.board.is_full():
                self.board.display()
                print("The game is a draw!")
                break
            
            # Switch to the other player
            self.switch_player()

# Main execution block
if __name__ == "__main__":
    player1 = Player("Player 1", "X")
    player2 = Player("Player 2", "O")
    game = Game(player1, player2)
    game.play()
