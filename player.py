# File: player.py
# This module defines the Player class.

class Player:
    """
    Represents a player in the game.
    A player has a name and a symbol ('X' or 'O').
    """
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
