# RockPaperScissors

## Gameplay

- The game follows the standard Rock, Paper, Scissors rules: Paper beats rock, rock beats scissors, and scissors beat paper.
- You can play against a computer player or watch two computer players compete.
- The game displays the results after each round and keeps track of the score.
- You can customize the number of rounds to play.

## Computer Player Strategies

The game includes different computer player strategies:

1. AlwaysRockPlayer: This player always plays 'rock'.
2. RandomPlayer: This player chooses moves randomly.
3. ReflectPlayer: This player imitates the human player's last move.
4. CyclePlayer: This player cycles through the three moves.

## How to Play

- When playing against a computer player, you'll be prompted to enter your move: rock, paper, or scissors.
- For computer vs. computer matches, just watch the game unfold.
- After the specified number of rounds, the game will announce the winner and display the final score.

## Code Structure

- `rps.py`: The main Python script that contains the game logic.
- `moves`: A list of valid moves in the game.
- `Player`: The base class for all player strategies.
- `HumanPlayer`: A subclass for human players.
- `RandomPlayer`: A subclass for computer players that choose moves randomly.
- `ReflectPlayer`: A subclass for computer players that imitate the human player's last move.
- `CyclePlayer`: A subclass for computer players that cycle through the moves.
- `beats()`: A function that determines the winner of a round based on the moves.

## Acknowledgments

- This project is a simplified implementation of the Rock, Paper, Scissors game.
- It is a great way to practice Python programming and object-oriented design.

## Author

Jemimah Bayode-Taylor under Udacity.

## License

This project is licensed under Udacity

Enjoy the game and have fun playing Rock, Paper, Scissors!
