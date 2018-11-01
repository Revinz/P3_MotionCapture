import argparse
import logging
import time
import importlib.util

import cv2
import numpy as np

import tf_pose.estimator as estimator
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh

# Import our stuff
import human_tetris as ht
import preprocess


logger = logging.getLogger('TfPoseEstimator-WebCam')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

fps_time = 0


# Game manager variable reference
GameManager = ht.Human_Tetris()

if __name__ == '__main__':

    #This part just parses the string input from the command line
    parser = argparse.ArgumentParser(description='tf-pose-estimation realtime webcam')
    parser.add_argument('--camera', type=int, default=0)

    parser.add_argument('--resize', type=str, default='0x0',
                        help='if provided, resize images before they are processed. default=0x0, Recommends : 432x368 or 656x368 or 1312x736 ')
    parser.add_argument('--resize-out-ratio', type=float, default=4.0,
                        help='if provided, resize heatmaps before they are post-processed. default=1.0')

    parser.add_argument('--model', type=str, default='mobilenet_thin', help='cmu / mobilenet_thin')
    parser.add_argument('--show-process', type=bool, default=False,
                        help='for debug purpose, if enabled, speed for inference is dropped.')
    args = parser.parse_args()

    logger.debug('initialization %s : %s' % (args.model, get_graph_path(args.model)))
    w, h = model_wh(args.resize)
    if w > 0 and h > 0:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))
    else:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(432, 368))
    logger.debug('cam read+')

    #Start the camera
    cam = cv2.VideoCapture(args.camera)
    ret_val, image = cam.read()
    logger.info('cam image=%dx%d' % (image.shape[1], image.shape[0]))

    pre = preprocess.Preprocessing();
    #Keep reading the camera input until you exit the program -- You can click ESC to quit the program while it is running
    while True:
        ret_val, image = cam.read()

        # Pre-processing
        preprocessed = pre.Preprocess(pre.HIGH_CONTRAST, image)
        
        # Detect Joints
        #logger.debug('image process+')
        humans = e.inference(preprocessed, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio) # Array of the humans with joints.
            
        #Draw joints -- will be hidden later. 
        #logger.debug('postprocess+')
        preprocessed = TfPoseEstimator.draw_humans(preprocessed, humans, imgcopy=False)


        # Update the players' joint positions
        for counter, human in enumerate(humans): #For the 2 players

            if counter > 1: #Don't bother detecting more than 2 players.
                break;

            #Update the body parts
            for part in human.body_parts:
                print(human.body_parts[part].uidx)
                print(counter)
                print("X= %f Y= %f" % (human.body_parts[part].x * 432, human.body_parts[part].y * 368))



        # Generate joint image with all the currently known joint locations

        # Show the image
        #logger.debug('show+')
        cv2.putText(preprocessed,
                    "FPS: %f" % (1.0 / (time.time() - fps_time)),
                    (10, 10),  cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 255, 0), 2)
        cv2.imshow('tf-pose-estimation result', preprocessed)
        fps_time = time.time()
        if cv2.waitKey(1) == 27:
            break
        logger.debug('finished+')


    cv2.destroyAllWindows()
