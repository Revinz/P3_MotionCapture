import tf_pose.estimator

class Person:
 

    # Part index values that OpenPose uses:
    """
    Nose = 0 ---
    Neck = 1 ---
    RShoulder = 2 ---
    RElbow = 3 ---
    RWrist = 4 ---
    LShoulder = 5 ---
    LElbow = 6 ---
    LWrist = 7 ---
    RHip = 8 ---
    RKnee = 9 ---
    RAnkle = 10 ---
    LHip = 11 ---
    LKnee = 12 ---
    LAnkle = 13 ---
    REye = 14
    LEye = 15
    REar = 16
    LEar = 17
    Background = 18
    """

    def __init__(self):
        self._leftWrist = (0, 0)
        self._leftElbow = (0, 0)
        print("New Person created")



class Human_Tetris:

    def __init__(self):       
        self.players = [Person(), Person()]
        self.counter = 0

    def __UpdatePlayers__(self, KeyPoints):

        # Update the players' joints individually only if there is a new replacement for them, otherwise keep the old one
        for player in self.players:
            continue



        return
