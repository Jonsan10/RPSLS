
#Parent
class Player:
    def __init__(self):
        self.name = '' 
        self.gestures_list = ['Rock', 'Paper', 'Scissors', 'Lizard','Spock']
        self.chosen_gesture= ''
        self.win_counter = 0

    def choose_gesture(self):
        pass
    def choose_name(self):
        pass
    def score_point(self):
        self.win_counter += 1
