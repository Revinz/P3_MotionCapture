import argparse
import logging
import time

import matplotlib.pyplot as plt

import cv2
import numpy as np

from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh

logger = logging.getLogger('TfPoseEstimator-Video')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

fps_time = 0

#for plotting
bodyPartCounter = 0  # Total amount of joints found
bodyPartSectionsCounter = []  # Amounts of joints per x frames

totalJoints = 0

frameJoints = 0

frame = -1

jointList = []
frameList = []


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tf-pose-estimation Video')
    parser.add_argument('--video', type=str, default='')
    parser.add_argument('--resolution', type=str, default='432x368', help='network input resolution. default=432x368')
    parser.add_argument('--model', type=str, default='mobilenet_thin', help='cmu / mobilenet_thin')
    parser.add_argument('--show-process', type=bool, default=False,
                        help='for debug purpose, if enabled, speed for inference is dropped.')
    parser.add_argument('--showBG', type=bool, default=True, help='False to show skeleton only.')
    args = parser.parse_args()

    logger.debug('initialization %s : %s' % (args.model, get_graph_path(args.model)))
    w, h = model_wh(args.resolution)
    e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))
    cap = cv2.VideoCapture(args.video)

    if cap.isOpened() is False:
        print("Error opening video stream or file")
    while cap.isOpened():
        ret_val, image = cap.read()

        humans = e.inference(image)
        if not args.showBG:
            image = np.zeros(image.shape)
        image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)

        cv2.putText(image, "FPS: %f" % (1.0 / (time.time() - fps_time)), (10, 10),  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.imshow('tf-pose-estimation result', image)
        fps_time = time.time()

        for human in enumerate(humans):


            bodyPartCounter += len(human.body_parts)
            # print("Total Parts found: " + bodyPartCounter)
            totalJoints = totalJoints + len(human.body_parts)
            
            frameJoints = frameJoints + len(human.body_parts)


            bodyPartSectionsCounter

        jointList.append(frameJoints)
        
        frameJoints = 0

        frameList.append(frame)

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    print("The total amount of joints found: " + str(totalJoints))
    print("Frame count: " + str(frame))
    plt.plot(frameList, jointList)
    plt.show()
logger.debug('finished+')
