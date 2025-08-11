Tic-Tac-Toe Game 🎮

This is a simple, command-line Tic-Tac-Toe game created in Python. It's built with an object-oriented approach, separating the game logic from the board's state and functions.

-----

  Features ✨

  * **Two-player mode:** Players can take turns entering their moves.
  * **Input validation:** The game checks for valid moves, preventing players from choosing an occupied space or an out-of-range position.
  * **Win condition checking:** The game automatically detects when a player has won.
  * **Draw condition checking:** It can also identify when the game has ended in a draw.
  * **Clear and simple interface:** The board is displayed clearly in the terminal, using a coordinate system (row and column).

-----

   Prerequisites 🛠️

To run this game, you only need **Python 3.x** installed on your computer.

-----
   
    How to Play ▶️

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/tictactoe-python.git
    ```
2.  **Navigate to the directory:**
    ```bash
    cd tictactoe-python
    ```
3.  **Run the game from your terminal:**
    ```bash
    python game.py
    ```
4.  Follow the on-screen instructions. When prompted, enter the **row** and **column** of the square you want to mark. The coordinates start at `0, 0` in the top-left corner.

-----

## Project Structure 📁

The game is organized into two main files for better modularity:

  * **`board.py`**: Contains the **`Board` class**, which manages the game's state. It handles displaying the board, placing symbols, and checking for win or draw conditions.
  * **`game.py`**: This is the main entry point for the game. It manages the game loop, switches between players, handles user input, and calls methods from the `Board` class to update and display the game.

-----

## Contributing 🤝

Feel free to fork this repository and submit pull requests to improve the game. You could add features like a single-player mode against an AI or a graphical user interface.

-----

## License 📜

This project is licensed under the MIT License.
