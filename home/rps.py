import random

# Define the moves using a dictionary for better readability
MOVES = {
    'rock': 'Rock',
    'paper': 'Paper',
    'scissors': 'Scissors',
    'spock': 'Spock',
    'lizard': 'Lizard'
}


# Define ANSI Escape Codes for terminal colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class AlwaysRockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(list(MOVES.keys()))


class ImitateHumanPlayer(Player):
    def __init__(self):
        self.human_move = None

    def move(self):
        if self.human_move:
            return self.human_move
        return random.choice(list(MOVES.keys()))

    def learn(self, my_move, their_move):
        self.human_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.move_index = 0

    def move(self):
        moves_list = list(MOVES.keys())
        move = moves_list[self.move_index]
        self.move_index = (self.move_index + 1) % len(MOVES)
        return move


class HumanPlayer(Player):
    def move(self):
        while True:
            rt = "Rock, Paper, Scissors, Spock, or Lizard? > "
            player_input = input(rt).lower()
            if player_input in MOVES:
                return player_input
            else:
                we = "Invalid move. Please choose from 'rock',"
                print("{we} 'paper', 'scissors', 'spock', or 'lizard'.")


class Game:
    def __init__(self, p1, p2, rounds):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0
        self.rounds = rounds
        self.current_round = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {Colors.BOLD}{MOVES[move1]}{Colors.ENDC}")
        print(f"Opponent played {Colors.BOLD}{MOVES[move2]}{Colors.ENDC}")

        if move1 == move2:
            print(f"{Colors.WARNING}** IT IS A TIE **{Colors.ENDC}")
        elif (move1 == 'rock' and move2 == 'scissors') or \
             (move1 == 'rock' and move2 == 'lizard') or \
             (move1 == 'paper' and move2 == 'rock') or \
             (move1 == 'paper' and move2 == 'spock') or \
             (move1 == 'scissors' and move2 == 'paper') or \
             (move1 == 'scissors' and move2 == 'lizard') or \
             (move1 == 'spock' and move2 == 'rock') or \
             (move1 == 'spock' and move2 == 'scissors') or \
             (move1 == 'lizard' and move2 == 'spock') or \
             (move1 == 'lizard' and move2 == 'paper'):
            print(f"{Colors.OKGREEN}** PLAYER ONE WINS **{Colors.ENDC}")
            self.p1_score += 1
        else:
            print(f"{Colors.FAIL}** PLAYER TWO WINS **{Colors.ENDC}")
            self.p2_score += 1
        self.current_round += 1
        tt = f"Score: Player one score {self.p1_score},"
        print(f"{tt} Player two score {self.p2_score}")

        # Call the remembering method for applicable players
        if isinstance(self.p1, ImitateHumanPlayer):
            self.p1.learn(move1, move2)
        if isinstance(self.p2, ImitateHumanPlayer):
            self.p2.learn(move2, move1)

    def play_match(self):
        print("Match start!")
        for round in range(self.rounds):
            print(f"\nRound {round + 1}:")
            self.play_round()
        print("MATCH OVER")
        print(f"Player 1 score: {self.p1_score}")
        print(f"Player 2 score: {self.p2_score}")
        if self.p1_score > self.p2_score:
            print(f"{Colors.HEADER}Player 1 wins the match!{Colors.ENDC}")
        elif self.p2_score > self.p1_score:
            print(f"{Colors.HEADER}Player 2 wins the match!{Colors.ENDC}")
        else:
            print(f"{Colors.HEADER}It's a tie!{Colors.ENDC}")


class Tournament:
    def __init__(self, players, rounds):
        self.players = players
        self.rounds = rounds
        self.results = {}

    def run_game(self, p1, p2):
        game = Game(p1, p2, self.rounds)
        game.play_match()
        if p1 not in self.results:
            self.results[p1] = 0
        if p2 not in self.results:
            self.results[p2] = 0
        if game.p1_score > game.p2_score:
            self.results[p1] += 1
        elif game.p2_score > game.p1_score:
            self.results[p2] += 1

    def run_tournament(self):
        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                self.run_game(self.players[i], self.players[j])


if __name__ == '__main__':
    # Create a list of player strategies
    player_strategies = [
        AlwaysRockPlayer(),
        RandomPlayer(),
        ImitateHumanPlayer(),
        CyclePlayer()
    ]

    # Ask the user to choose their player
    print("Choose a player strategy:")
    for i, player in enumerate(player_strategies):
        print(f"{i + 1}. {player.__class__.__name__}")

    while True:
        try:
            choice = int(input("Enter the number of your chosen player: "))
            if 1 <= choice <= len(player_strategies):
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Specify the number of rounds for the match
    rounds = 3  # You can change the number of rounds

    # Create the list of players with the user's choice
    players = [HumanPlayer()]  # Human player always comes first
    players.append(player_strategies[choice - 1])

    # Run the tournament
    tournament = Tournament(players, rounds)
    tournament.run_tournament()

    print("Tournament Results:")
    for player, wins in tournament.results.items():
        print(f"{player.__class__.__name__}: {wins} wins")

    winner = max(tournament.results, key=tournament.results.get)
    print(f"The winning strategy is {winner.__class__.__name__}")
