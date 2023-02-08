#! /usr/bin/env python
# -*- coding:utf-8 -*-
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

        self.steering_delta_pub = rospy.Publisher("/lane/delta_lane_x", Int32, queue_size=1) # 각 차선들 평균의 x좌표 변화량 publish

        self.YELLOW_LANE_LOW = np.array([5,90,179]) # HLS로 처리 (노란색 차선)
        self.YELLOW_LANE_HIGH = np.array([35,255,255])

        self.WHITE_LANE_LOW = np.array([0,200,0]) # HLS로 처리 (흰색 차선)
        self.WHITE_LANE_HIGH = np.array([179,255,255])


    def Image_process_callback(self, img):
        self.frame = self.cvbridge.imgmsg_to_cv2(img, "bgr8") # opencv 이미지로 변환

        self.up_cropped_image, self.down_cropped_image = self.image_crop(self.frame) # 이미지 crop

        self.up_yellow_thresholded_image, self.down_yellow_thresholded_image = self.color_detect_yellow(self.up_cropped_image, self.down_cropped_image) # 노란색 중앙선 색상 검출
        self.up_white_thresholded_image, self.down_white_thresholded_image = self.color_detect_white(self.up_cropped_image, self.down_cropped_image) # 흰색 차선 색상 검출

        self.up_yellow_x = self.calc_distance(self.up_yellow_thresholded_image) # 위쪽 노란색 중앙선의 x좌표 계산 (차선의 무게 중심의 x좌표)
        self.up_white_x = self.calc_distance(self.up_white_thresholded_image) # 위쪽 흰색 차선의 x좌표 계산 (차선의 무게 중심의 x좌표)
        self.down_yellow_x = self.calc_distance(self.down_yellow_thresholded_image) # 아래쪽 노란색 중앙선의 x좌표 계산 (차선의 무게 중심의 x좌표)
        self.down_white_x = self.calc_distance(self.down_white_thresholded_image) # 아래쪽 흰색 차선의 x좌표 계산 (차선의 무게 중심의 x좌표)

        self.up_lane_x_mean = (self.up_yellow_x + self.up_white_x)/2
        self.down_lane_x_mean = (self.down_yellow_x + self.down_white_x)/2

        self.delta_lanes_x = self.up_lane_x_mean - self.down_lane_x_mean

        self.steering_delta_pub.publish(self.delta_lanes_x)
        
        viz = True
        #visualization
        if viz:
            self.viz_result()

            
    def calc_distance(self, b_image):
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
        #cv2.imshow('left cropped image',self.left_cropped_image)
        #cv2.imshow('right cropped image',self.right_cropped_image)
        #cv2.imshow('left color_detect',self.left_thresholded_image)
        #cv2.imshow('right color_detect',self.right_thresholded_image)
        #self.mask_yellow = cv2.circle(self.left_thresholded_image,(self.left_x,30),10,(0,0,0),-1)
        #self.mask_white = cv2.circle(self.right_thresholded_image,(self.right_x,30),10,(0,0,0),-1)
        #cv2.imshow('yellow_color_detect_circle',self.mask_yellow)
        #cv2.imshow('white_color_detect_circle',self.mask_white)
        cv2.imshow('down yellow lane image', self.down_yellow_thresholded_image)
        cv2.imshow('down white lane image', self.down_white_thresholded_image)
        cv2.imshow('up yellow lane image', self.up_yellow_thresholded_image)
        cv2.imshow('up white lane image', self.up_white_thresholded_image)
        cv2.waitKey(1)
            
    def image_crop(self, input_image):
        return input_image[420:430, 0:640], input_image[450:480, 0:640]

    def color_detect_yellow(self, up_Y_img, down_Y_img):
        up_yellow_hls = cv2.cvtColor(up_Y_img, cv2.COLOR_BGR2HLS)
        down_yellow_hls = cv2.cvtColor(down_Y_img, cv2.COLOR_BGR2HLS)
        mask_up_yellow = cv2.inRange(up_yellow_hls, self.YELLOW_LANE_LOW, self.YELLOW_LANE_HIGH) # 왼쪽 중앙차선 (노란색)
        mask_down_yellow = cv2.inRange(down_yellow_hls, self.YELLOW_LANE_LOW, self.YELLOW_LANE_HIGH) # 오른쪽 차선 (흰색)
        return mask_up_yellow, mask_down_yellow
    
    def color_detect_white(self, up_W_img, down_W_img):
        up_white_hls = cv2.cvtColor(up_W_img, cv2.COLOR_BGR2HLS)
        down_white_hls = cv2.cvtColor(down_W_img, cv2.COLOR_BGR2HLS)
        mask_up_white = cv2.inRange(up_white_hls, self.WHITE_LANE_LOW, self.WHITE_LANE_HIGH) # 왼쪽 중앙차선 (노란색)
        mask_down_white = cv2.inRange(down_white_hls, self.WHITE_LANE_LOW, self.WHITE_LANE_HIGH) # 오른쪽 차선 (흰색)
        return mask_up_white, mask_down_white



if __name__ == '__main__':
    a = LaneDetection()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("program down")
