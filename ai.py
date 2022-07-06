from player import Player
import random
#child
class AI(Player):
    def __init__(self):
      super().__init__()


    def choose_gesture (self):
            print('AI choses:')
            self.chosen_gesture= random.choice(self.gestures_list)
            print (self.chosen_gesture)
    
    def choose_name(self):
        self.name = 'Bob'