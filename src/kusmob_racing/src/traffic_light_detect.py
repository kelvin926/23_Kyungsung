#! /usr/bin/env python
# -*- coding:utf-8 -*-

import cv2
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import String
import rospy
from cv_bridge import CvBridge

class TrafficDetection:
    def __init__(self):
        rospy.init_node("traffic_detect_node")

        self.cvbridge = CvBridge()
        rospy.Subscriber("/camera/color/image_raw", Image, self.Image_process_callback_T) # 원본 이미지 받는거?

        self.color_king = rospy.Publisher("/traffic_light", String, queue_size=1)

        self.RED_LIGHT_LOW = np.array([150,50,30]) # 빨간불 범위
        self.RED_LIGHT_HIGH = np.array([180,255,255])

        self.GREEN_LIGHT_LOW = np.array([50,50,30]) # 초록불 범위
        self.GREEN_LIGHT_HIGH = np.array([80,255,255])

        self.BLUE_SIGN_LOW = np.array([100,100,100]) # 파란 주차 표지판 범위
        self.BLUE_SIGN_HIGH = np.array([150,255,255])


    def Image_process_callback_T(self, img):
        self.frame_T = self.cvbridge.imgmsg_to_cv2(img, "bgr8") # opencv 이미지로 변환

        self.traffic_cropped_image = self.image_crop_T(self.frame_T) # 이미지 crop

        self.imgcolor_red, self.imgcolor_green, self.imgcolor_blue = self.color_detect_T(self.traffic_cropped_image) # 신호등 색상 검출

        self.check_color() # 신호등 색상 판단
        self.color_king.publish(self.now_color)

        viz = True
        #visualization
        if viz:
            self.viz_result()
    
    def viz_result(self):
        cv2.imshow('traffic original image',self.frame_T)
        cv2.imshow('traffic color RED',self.imgcolor_red)
        cv2.imshow('traffic color GREEN',self.imgcolor_green)
        cv2.imshow('traffic color BLUE', self.imgcolor_blue)
        cv2.waitKey(1)

    def image_crop_T(self, input_image):
        return input_image[0:300, 400:640] # 대충 오른쪽 위쪽 잡았는데..

    def color_detect_T(self, cropped_img):
        traffic_hsv = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2HSV)
        self.mask_red = cv2.inRange(traffic_hsv, self.RED_LIGHT_LOW, self.RED_LIGHT_HIGH) 
        self.mask_green = cv2.inRange(traffic_hsv, self.GREEN_LIGHT_LOW, self.GREEN_LIGHT_HIGH) 
        self.mask_blue = cv2.inRange(traffic_hsv, self.BLUE_SIGN_LOW, self.BLUE_SIGN_HIGH)

        res_red = cv2.bitwise_and(cropped_img, cropped_img, mask = self.mask_red)
        res_green = cv2.bitwise_and(cropped_img, cropped_img, mask = self.mask_green)
        res_blue = cv2.bitwise_and(cropped_img, cropped_img, mask = self.mask_blue)
        return res_red, res_green, res_blue
    
    def check_color(self):
        self.red_size = np.sum(self.mask_red)/np.size(self.mask_red)
        self.green_size = np.sum(self.mask_green)/np.size(self.mask_green)
        self.blue_size = np.sum(self.mask_blue)/np.size(self.mask_blue)

        if (self.red_size >= 6) and (self.red_size > self.green_size) and (self.red_size > self.blue_size):
            print("COLOR : RED")
            self.now_color = "red"
        elif (self.green_size >= 6) and (self.green_size > self.red_size) and (self.green_size > self.blue_size):
            print("COLOR : GREEN")
            self.now_color = "green"
        elif (self.blue_size >= 6) and (self.blue_size > self.red_size) and (self.blue_size > self.green_size):
            print("COLOR : BLUE")
            self.now_color = "blue"
        else:
            print("NONE")
            self.now_color = "none"

        return self.now_color

if __name__ == '__main__':
    a = TrafficDetection()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("program down")
