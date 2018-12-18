
import argparse
import logging
import time

import matplotlib.pyplot as plt

import cv2
import numpy as np

from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh

import preprocess
import counterJoints

logger = logging.getLogger('TfPoseEstimator-Video')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

fps_time = 0
fps_found = False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tf-pose-estimation Video')
    parser.add_argument('--video', type=str, default='test.mp4')
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

    pre = preprocess.Preprocessing();
    jc = counterJoints.JointsCounter();

    if cap.isOpened() is False:
        print("Error opening video stream or file")
    while cap.isOpened():
        ret_val, image = cap.read()      

        jc.frame += 1

        #preprocessed = pre.Contrast(0.75,image) ##Change the pre.XXXX to the preprocessing technique you want. 
        #preprocessed = pre.Contrast(1.25,image) #HIGH CONTRAST

        #preprocessed = pre.Edge_detection(image)
        #FIRST ITERATION: 100, 150
        #SECOND ITERATION: 75, 150

        #preprocessed = pre.Histogram_EQ(image)
        #FIRST ITERATION:

        preprocessed = pre.Sharpness(6.5,4,image)
        # Default values: 5, 4
        #FIRST ITERATION: 9, 9
        #SECOND ITERATION: 6.5,4

        image = preprocessed #Outcomment this to only have openpose (groundtruth)

        humans = e.inference(image, resize_to_default=True, upsample_size=4.0)

        if not args.showBG:
            image = np.zeros(image.shape)
        image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)

        cv2.putText(image, "Frame: " + str(jc.frame), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.putText(image, "FPS: %f" % (1.0 / (time.time() - fps_time)), (10, 10),  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.imshow('tf-pose-estimation result', image)
        fps = 1/(time.time() - fps_time)
        fps_time = time.time()

        #Update FPS measurements
        if fps_found == False and fps > 1:
            print(fps)
            fps_found = True
            highest_fps = fps           
            lowest_fps = fps
        
        if fps_found:
            if fps > highest_fps:
                highest_fps = fps
            elif fps < lowest_fps:
                lowest_fps

        #Count joints for the frame
        jc.CountJoints(humans)

        if cv2.waitKey(1) == 27:
            break

        #Stop video after 300 frames -- otherwise it might result in an error
        if (jc.frame >= 300):
            break
            
    cv2.destroyAllWindows()
    print("Lowest FPS: %f" % lowest_fps)
    print("Highest FPS: %f" % highest_fps)
    print("Variance: %f" % (highest_fps - lowest_fps))
    jc.ShowJointPlot()
logger.debug('finished+')
