from player import Player
#child
class AI(Player):
    def __init__(self,name, win_counter):
        super().__init__(name, win_counter)

    def choose_gesture(self):
        print('rock, paper, scissors, lizards, spock')
        return self.gester_list[0]
        
    print(choose_gesture)
