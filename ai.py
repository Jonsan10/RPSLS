from player import Player
import random
#child
class AI(Player):
    def __init__(self):
        #self.choose_gesture()
        super().__init__()


    def choose_gesture (self):
            print('Rock, Paper, Scissors, Lizard, Spock')
            #self.get_gesture = self.gestures_list
            self.chosen_gesture= random.choice(self.gestures_list)
            print (self.chosen_gesture)
    
