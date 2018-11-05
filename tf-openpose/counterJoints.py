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
              
counter = 0
              
for player in self.players:
  counter+=len(player.body_parts)
    
                
             
print(counter)
