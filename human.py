from player import Player
#child
class Human(Player):
    def __init__(self):
        super().__init__()
        
    def choose_name(self, player_num):
        self.name = input(f'player {player_num} please enter your name: ')
        print(f'Welcome {self.name}!')


    def choose_gesture (self):
        
        # (validate the user's selection)

        for num in range(0, len(self.gestures_list)):
            print(f'{num} {self.gestures_list[num]}')   

        
        user_selection = int(input('Please use the number keys to enter your gesture selection:  '))
        # if user_selection <= 5:
        #         self.choose_gesture = self.gestures_list[user_selection]
        #         print(f'Nicely done {self.name}, you have selected {self.chosen_gesture}')
        # else:
        #      print('invalid value.')
        #      return
        
        self.chosen_gesture = self.gestures_list[user_selection]
        print(f'Nicely done {self.name}, you have selected {self.chosen_gesture}')
           
