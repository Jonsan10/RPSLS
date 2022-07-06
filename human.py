from player import Player
#child
class Human(Player):
    def __init__(self):
        super().__init__()
        
def choose_gesture (self):
    # present gesture options to user
    # capture user's selection
    # index the gestures list with the user's selection
    # display user's selection to user

    # (validate the user's selection)

    for num in range(0, len(self.gestures_list)):
        print(f'{num} {self.gestures_list[num]}')

    user_selection = int(input('Please use the number keys to enter your gesture selection:  '))
    self.chosen_gesture = self.gestures_list[user_selection]
    print(f'Nicely done {self.name}, you have selected {self.chosen_gesture}')
           
