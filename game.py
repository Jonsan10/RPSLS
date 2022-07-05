from human import Human
from ai import AI
class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = AI()
        self.grettings()
        self.rules()
        self.game_mode()
        self.run_game()
        self.display_winner()

    def greetings(self):
        print('Welcome to RPSLS')

    def rules(self):
        print('Rules of the game are, Scissors cuts Paper,')

    def game_mode(self):
        pass

    def run_game(self):
        pass

    def display_winner(self):
        pass