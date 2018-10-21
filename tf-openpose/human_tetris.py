
class Person:
   
    # Joint list in form of screen coordinates
    _leftWrist = (0, 0)
    _leftElbow = (0, 0)

    def __init__(self):
        self._leftWrist = (0, 0)
        self._leftElbow = (0, 0)
        print("New Person created")


class Human_Tetris:

    counter = 0

    def __init__(self):       
        self.players = [Person(), Person()]
        self.counter = 0

    def __UpdatePlayers__(self, KeyPoints):

        # Update the players' joints individually only if there is a new replacement for them, otherwise keep the old one
        for player in self.players:
            continue



        return
