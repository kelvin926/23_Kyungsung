#! /usr/bin/env python

import cv2
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import Int32
import rospy
from cv_bridge import CvBridge
class LaneDetection:
    def __init__(self):
        rospy.init_node("lane_detect_node")
       
        self.cvbridge = CvBridge()
        rospy.Subscriber("/camera/color/image_raw", Image, self.Image_process_callback)
        self.steering_pub = rospy.Publisher("/lane/left_lane_x", Int32, queue_size=1)
        self.YELLOW_LANE_LOW = np.array([5,90,179])
        self.YELLOW_LANE_HIGH = np.array([35,255,255])


    def Image_process_callback(self, img):
        self.frame = self.cvbridge.imgmsg_to_cv2(img, "bgr8")
        self.cropped_image = self.image_crop(self.frame)
        self.thresholded_image = self.color_detect(self.cropped_image)
        self.left_x = self.calc_left_distance(self.thresholded_image)
        self.steering_pub.publish(self.left_x)
        
        viz = True
        #visualization
        if viz:
            self.viz_result()
           
            
    def calc_left_distance(self, b_image):
        try:
            M = cv2.moments(b_image)
            self.x = int(M['m10']/M['m00'])
            self.y = int(M['m01']/M['m00'])
        except:
            self.x = -1
            self.y = -1
        # print("x, y = {}, {}".format(x, y))
        return self.x
    
    def viz_result(self):
        
        cv2.imshow('original image',self.frame)
        cv2.imshow('cropped image',self.cropped_image)
        cv2.imshow('color_detect',self.thresholded_image)
        self.mask_yellow = cv2.circle(self.thresholded_image,(self.left_x,30),10,(0,0,0),-1)
        cv2.imshow('color_detect_circle',self.mask_yellow)
        cv2.waitKey(1)
            
    def image_crop(self, input_image):
        return input_image[420:480, 0:320]

 
    def color_detect(self, img):
        # print(self.YELLOW_LANE_LOW)
        # print(self.YELLOW_LANE_HIGH)
        hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
        mask_yellow = cv2.inRange(hls, self.YELLOW_LANE_LOW, self.YELLOW_LANE_HIGH)
        # cv2.imshow("hls", hls)
        # cv2.imshow("mask_yellow", mask_yellow)
        # cv2.imshow("h", hls[:,:,0])
        # cv2.imshow("s", hls[:,:,1])
        # cv2.imshow("v", hls[:,:,2])
        # cv2.waitKey(1)
        # return mask_white
        return mask_yellow
        # return mask


if __name__ == '__main__':
    a = LaneDetection()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("program down")
