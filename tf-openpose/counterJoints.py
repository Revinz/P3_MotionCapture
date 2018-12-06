
import matplotlib.pyplot as plt

class JointsCounter:

    #for plotting
    bodyPartCounter = 0  # Total amount of joints found
    bodyPartSectionsCounter = []  # Amounts of joints per x frames

    totalJoints = 0

    frameJoints = 0

    frame = 0

    jointList = []
    frameList = []

    frame = 0

    showPlot = False

    def CountJoints(self, humans):
        for counter, human in enumerate(humans): #For the 2 players

            self.bodyPartCounter+=len(human.body_parts)
            #print("Total Parts found: " + bodyPartCounter)
            self.totalJoints = self.totalJoints + len(human.body_parts)
            
            self.frameJoints = self.frameJoints + len(human.body_parts)

            self.bodyPartSectionsCounter
            
        self.jointList.append(self.frameJoints)
        
        self.frameJoints = 0

        self.frameList.append(self.frame)

    def ShowJointPlot(self):
        if not self.totalJoints > 0:
            return

        print("The total amount of joints found: " + str(self.totalJoints))
        print("Frame count: " + str(self.frame))
        plt.plot(self.frameList, self.jointList)
        plt.xlabel('Frame')
        plt.ylabel('Body parts found')
        plt.title('Body parts found per frame')
        plt.grid(True)
        plt.show()