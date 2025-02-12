#!/usr/bin/env python3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Sample code for Comp24011 SLAM lab solution

NB: The default code in non-functional; it simply avoids type errors
"""

__author__ = "USERNAME"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import cv2
import sys

from vision_tasks_base import VisionTasksBase

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class VisionTasks(VisionTasksBase):
    def __init__(self, *params):
        """Initialise instance by passing arguments to super class"""
        super().__init__(*params)

    def dt_matching(self, prev_image, this_image):
        """Implements feature matching based on distance thresholding

        :param prev_image: cv2 image of previous frame
        :type prev_image:  cv2.Mat == numpy.ndarray
        :param this_image: cv2 image of current frame
        :type this_image:  cv2.Mat == numpy.ndarray

        :return: keypoints of previous frame,
                 keypoints of current frame,
                 matches for feature_id descriptors
        :rtype:  list[cv2.KeyPoint],
                 list[cv2.KeyPoint],
                 list[list[vision_tasks_base.DMatch]]
        """
        return [], [], []

    def nn_matching(self, prev_image, this_image):
        """Implements feature matching based on nearest neighbour

        :param prev_image: cv2 image of previous frame
        :type prev_image:  cv2.Mat == numpy.ndarray
        :param this_image: cv2 image of current frame
        :type this_image:  cv2.Mat == numpy.ndarray

        :return: keypoints of previous frame,
                 keypoints of current frame,
                 matches for feature_id descriptors
        :rtype:  list[cv2.KeyPoint],
                 list[cv2.KeyPoint],
                 list[list[vision_tasks_base.DMatch]]
        """
        return [], [], []

    def nndr_matching(self, prev_image, this_image):
        """Implements feature matching based on nearest neighbour distance ratio

        :param prev_image: cv2 image of previous frame
        :type prev_image:  cv2.Mat == numpy.ndarray
        :param this_image: cv2 image of current frame
        :type this_image:  cv2.Mat == numpy.ndarray

        :return: keypoints of previous frame,
                 keypoints of current frame,
                 matches for feature_id descriptors
        :rtype:  list[cv2.KeyPoint],
                 list[cv2.KeyPoint],
                 list[list[vision_tasks_base.DMatch]]
        """
        return [], [], []

    def matchLocating(self, this_image, prev_image, prev_feature):
        """Calculates coordinates of a feature and
           its matches under the current matching algorithm

        :param this_image: cv2 image of current frame
        :type this_image:  cv2.Mat == numpy.ndarray
        :param prev_image: cv2 image of previous frame
        :type prev_image:  cv2.Mat == numpy.ndarray
        :param prev_feature: feature_id for previous frame descriptor
        :type prev_feature:  int

        :return: coordinate of feature in previous frame,
                 coordinates for feature matches in current frame
        :rtype:  tuple[int,int],
                 list[tuple[int,int]]
        """
        return (0,0), []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et sw=4 ts=4:
