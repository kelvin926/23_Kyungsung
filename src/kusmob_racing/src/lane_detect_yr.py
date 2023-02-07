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

        self.steering_up_pub = rospy.Publisher("/lane/up_lane_x", Int32, queue_size=1) # 위쪽 차선의 x좌표 평균을 publish
        self.steering_down_pub = rospy.Publisher("/lane/down_lane_x", Int32, queue_size=1) # 아래쪽 차선의 x좌표 평균을 publish


        self.YELLOW_LANE_LOW = np.array([5,90,179]) # HLS로 처리 (노란색 차선)
        self.YELLOW_LANE_HIGH = np.array([35,255,255])

        self.WHITE_LANE_LOW = np.array([0,200,0]) # HLS로 처리 (흰색 차선)
        self.WHITE_LANE_HIGH = np.array([179,255,255])


    def Image_process_callback(self, img):
        self.frame = self.cvbridge.imgmsg_to_cv2(img, "bgr8") # opencv 이미지로 변환

        self.left_up_cropped_image, self.right_up_cropped_image, self.left_down_cropped_image, self.right_down_cropped_image = self.image_crop(self.frame) # 4개 이미지 crop

        self.left_big_cropped_image, self.right_big_cropped_image = self.image_crop2(self.frame) # 큰 2개 이미지 crop

        self.left_up_thresholded_image, self.right_up_thresholded_image, self.left_down_thresholded_image, self.right_down_thresholded_image = self.color_detect(self.left_up_cropped_image, self.right_up_cropped_image, self.left_down_cropped_image, self.right_down_cropped_image) # 4개 색상 검출

        self.left_yellow_image, self.right_white_image = self.color_detect2(self.left_big_cropped_image, self.right_big_cropped_image) # 큰 2개 이미지 색상 검출

        self.left_up_x = self.calc_distance(self.left_up_thresholded_image) # 왼쪽 위 차선의 x좌표 계산 (차선의 무게 중심의 x좌표)
        self.right_up_x = self.calc_distance(self.right_up_thresholded_image) # 오른쪽 위 차선의 x좌표 계산 (차선의 무게 중심의 x좌표)
        self.left_down_x = self.calc_distance(self.left_down_thresholded_image) # 왼쪽 아래 차선의 x좌표 계산 (차선의 무게 중심의 x좌표)
        self.right_down_x = self.calc_distance(self.right_down_thresholded_image) # 오른쪽 아래 차선의 x좌표 계산 (차선의 무게 중심의 x좌표)
        
        self.up_lane_x_mean = (self.left_up_x + self.right_up_x)/2
        self.down_lane_x_mean = (self.left_down_x + self.right_down_x)/2
        

        self.steering_up_pub.publish(self.up_lane_x_mean)  # 위쪽 차선의 평균 전달
        self.steering_down_pub.publish(self.down_lane_x_mean) # 아래쪽 차선의 평균 전달
        
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
        cv2.imshow('left yellow lane', self.left_yellow_image)
        cv2.imshow('right white lane', self.right_white_image)
        cv2.waitKey(1)
            
    def image_crop(self, input_image):
        return input_image[420:430, 0:320], input_image[420:430, 321:640], input_image[460:480, 0:320], input_image[460:480, 321:640]
    
    def image_crop2(self,input_image2):
        return input_image2[420:480, 0:320], input_image2[420:480, 321:640]

    def color_detect(self, left_up_img, right_up_img, left_down_img, right_down_img):
        left_up_hls = cv2.cvtColor(left_up_img, cv2.COLOR_BGR2HLS)
        right_up_hls = cv2.cvtColor(right_up_img, cv2.COLOR_BGR2HLS)
        left_down_hls = cv2.cvtColor(left_down_img, cv2.COLOR_BGR2HLS)
        right_down_hls = cv2.cvtColor(right_down_img, cv2.COLOR_BGR2HLS)
        mask_left_up_yellow = cv2.inRange(left_up_hls, self.YELLOW_LANE_LOW, self.YELLOW_LANE_HIGH) # 왼쪽 위 중앙차선 (노란색)
        mask_right_up_white = cv2.inRange(right_up_hls, self.WHITE_LANE_LOW, self.WHITE_LANE_HIGH) # 오른쪽 위 차선 (흰색)
        mask_left_down_yellow = cv2.inRange(left_down_hls, self.YELLOW_LANE_LOW, self.YELLOW_LANE_HIGH) # 왼쪽 아래 중앙차선 (노란색)
        mask_right_down_white = cv2.inRange(right_down_hls, self.YELLOW_LANE_LOW, self.YELLOW_LANE_HIGH) # 오른쪽 아래 차선 (흰색)    
        return mask_left_up_yellow, mask_right_up_white, mask_left_down_yellow, mask_right_down_white
    
    def color_detect2(self, left_big_img, right_big_img):
        left_big_hls = cv2.cvtColor(left_big_img, cv2.COLOR_BGR2HLS)
        right_big_hls = cv2.cvtColor(right_big_img, cv2.COLOR_BGR2HLS)
        mask_left_big_yellow = cv2.inRange(left_big_hls, self.YELLOW_LANE_LOW, self.YELLOW_LANE_HIGH) # 왼쪽 중앙차선 (노란색)
        mask_right_big_white = cv2.inRange(right_big_hls, self.WHITE_LANE_LOW, self.WHITE_LANE_HIGH) # 오른쪽 차선 (흰색)
        res_left_yellow = cv2.bitwise_and(left_big_img, left_big_img, mask = mask_left_big_yellow)
        res_right_white = cv2.bitwise_and(right_big_img, right_big_img, mask = mask_right_big_white)
        return res_left_yellow, res_right_white



if __name__ == '__main__':
    a = LaneDetection()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("program down")