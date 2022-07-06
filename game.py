from human import Human
from ai import AI
class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = AI()

    def greetings(self):
        print('Welcome to RPSLS')

    def rules(self):
        print('Rules of the game are, Scissors cuts Paper,\n ,Paper covers Rock, \n Lizard poisons Spock, \n Spock smashes Scissors \n Scissors decapitates Lizard, \n Lizard eats Paper, \n Paper disproves Spock, \n Spock vaporizes Rock, \n Rock crushes Scissors')

    def setup_game(self):
        # Capture game mode selection from user (input())
        user_selection = input('please select 1 for single player or select 2 for Mulit player ')

        # if user selection is 2 (m-plyr) then p2 = human
        if user_selection == '2':
            self.player2 = Human()
        elif user_selection == '1':
            self.player1 = Human()
        else:
            return

            
        # display game mode
        self.player1.choose_name(;name)
        self.player2.choose_name()
    

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
            #compare the gestures
    
    def compare_gestures(self):
        gesture_1 = self.player1.chosen_gesture
        gesture_2 = self.player2.chosen_gesture

        if gesture_1 == gesture_2:
            pass
        elif gesture_1 == 'Rock':
            if gesture_2 == 'Scissors' or gesture_2 == 'Lizard':
                self.player1.score_point()
            else:
                self.player2.score_point()

        elif gesture_1 == 'Paper':
            if gesture_2 == 'Spock' or gesture_2 == 'Rock':
                self.player1.score_point()
            else: self.player2.score_point()

        elif gesture_1 == 'Scissors':
            if gesture_2 == 'Paper' or gesture_2 == 'Lizard':
                self.player1.score_point()
            else: self.player2.score_point()

        elif gesture_1 == 'Lizard':
            if gesture_2 == 'Paper' or gesture_2 == 'Spock':
                self.player1.score_point()
            else: self.player2.score_point()

        elif gesture_1 == 'Spock':
            if gesture_2 == 'Rock' or gesture_2 == 'Scissors':
                self.player1.score_point()
            else: self.player2.score_point()


    def display_winner(self):
        if self.player1.win_counter == 2:
            print(f'Congradualtions {self.player1} has won the game')
        elif self.player2.win_counter == 2:
            print(f'Congrats {self.player2} has won the game')