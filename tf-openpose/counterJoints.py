
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

    def CountJoints(self, humans):
        for counter, human in enumerate(humans): #For the 2 players

            bodyPartCounter+=len(human.body_parts)
            #print("Total Parts found: " + bodyPartCounter)
            totalJoints = totalJoints + len(human.body_parts)
            
            frameJoints = frameJoints + len(human.body_parts)

            bodyPartSectionsCounter
            
        jointList.append(frameJoints)
        
        frameJoints = 0

        frameList.append(frame)

