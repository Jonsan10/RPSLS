from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = AI()

    def greetings(self):
        print('Hello and welcome to the tantalizing game of ROCK PAPER SCISSORS LIZARD SPOCK! \nThe tournament winner will be the player who wins the best of three (3) matches for ultimate bragging rights.\nMay the odds be ever in your favor!')

    def rules(self):
        print('Rules of the game are simple and are as follows:\nScissors cuts Paper\nPaper covers Rock\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\nRock crushes Scissors')

    def setup_game(self):
        # Capture game mode selection from user (input())
        user_selection = input('Please select either 1 for single player or 2 for a multiplayer match: ')

        # if user selection is 2 (m-plyr) then p2 = human
        if user_selection == '2':
            self.player2 = Human()
        #elif user_selection == '1':
            #self.player2 = AI()
        #else:
           # return

            
        # display game mode
        self.player1.choose_name(player_num=1)
        self.player2.choose_name(player_num=2)
    

    def run_game(self):
        self.greetings()
        self.rules()
        self.setup_game()
        self.start_game()
        self.display_winner()
        
    def start_game(self):
    
        while self.player1.win_counter < 2 and self.player2.win_counter < 2:
            self.player1.choose_gesture()
            self.player2.choose_gesture()
            self.compare_gestures()

    
    def compare_gestures(self):
        gesture_1 = self.player1.chosen_gesture
        gesture_2 = self.player2.chosen_gesture

        if gesture_1 == gesture_2:
            print('This is a tie, no winner!')
            pass
        elif gesture_1 == 'Rock':
            if gesture_2 == 'Scissors' or gesture_2 == 'Lizard':
                self.player1.score_point()
                print(f'{self.player1.name} has won the round')
            else:
                self.player2.score_point()
                print(f'{self.player2.name} has won the round')

        elif gesture_1 == 'Paper':
            if gesture_2 == 'Spock' or gesture_2 == 'Rock':
                self.player1.score_point()
                print(f'{self.player1.name} has won the round')
            else: 
                self.player2.score_point()
                print(f'{self.player2.name} has won the round')

        elif gesture_1 == 'Scissors':
            if gesture_2 == 'Paper' or gesture_2 == 'Lizard':
                self.player1.score_point()
                print(f'{self.player1.name} has won the round')
            else: 
                self.player2.score_point()
                print(f'{self.player2.name} has won the round')

        elif gesture_1 == 'Lizard':
            if gesture_2 == 'Paper' or gesture_2 == 'Spock':
                self.player1.score_point()
                print(f'{self.player1.name} has won the round')
            else: 
                self.player2.score_point()
                print(f'{self.player2.name} has won the round')

        elif gesture_1 == 'Spock':
            if gesture_2 == 'Rock' or gesture_2 == 'Scissors':
                self.player1.score_point()
                print(f'{self.player1.name} has won the round')
            else: 
                self.player2.score_point()
                print(f'{self.player2.name} has won the round')


    def display_winner(self):
        if self.player1.win_counter == 2:
            print(f'Well, well, well, {self.player1.name}! The odds WERE ever in your favor, you have won the game.')
        elif self.player2.win_counter == 2:
            print(f'{self.player2.name}, do the celebration dance, you have won the game!')