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

        self.steering_left_pub = rospy.Publisher("/lane/left_lane_x", Int32, queue_size=1) # 차선의 왼쪽 x좌표를 publish
        self.steering_right_pub = rospy.Publisher("/lane/right_lane_x", Int32, queue_size=1) # 차선의 오른쪽 x좌표를 publish


        self.YELLOW_LANE_LOW = np.array([5,90,179]) # BGR로 처리 (노란색 차선)
        self.YELLOW_LANE_HIGH = np.array([35,255,255])

        self.WHITE_LANE_LOW = np.array([200,200,200]) # BGR로 처리 (흰색 차선)
        self.WHITE_LANE_HIGH = np.array([255,255,255])


    def Image_process_callback(self, img):
        self.frame = self.cvbridge.imgmsg_to_cv2(img, "bgr8") # opencv 이미지로 변환

        self.left_cropped_image, self.right_cropped_image = self.image_crop(self.frame) # 이미지 crop

        self.left_thresholded_image, self.right_thresholded_image = self.color_detect(self.left_cropped_image, self.right_cropped_image) # 색상 검출

        self.left_x = self.calc_distance(self.left_thresholded_image) # 왼쪽 차선의 x좌표 계산 (차선의 무게 중심의 x좌표)
        self.right_x = self.calc_distance(self.right_thresholded_image) # 오른쪽 차선의 x좌표 계산 (차선의 무게 중심의 x좌표)

        self.steering_left_pub.publish(self.left_x)
        self.steering_right_pub.publish(self.right_x)
        
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
        cv2.imshow('left cropped image',self.left_cropped_image)
        cv2.imshow('right cropped image',self.right_cropped_image)
        cv2.imshow('left color_detect',self.left_thresholded_image)
        cv2.imshow('right color_detect',self.right_thresholded_image)
        self.mask_yellow = cv2.circle(self.left_thresholded_image,(self.left_x,30),10,(0,0,0),-1)
        self.mask_white = cv2.circle(self.right_thresholded_image,(self.right_x,30),10,(0,0,0),-1)
        cv2.imshow('yellow_color_detect_circle',self.mask_yellow)
        cv2.imshow('white_color_detect_circle',self.mask_white)
        cv2.waitKey(1)
            
    def image_crop(self, input_image):
        return input_image[420:480, 0:320], input_image[420:480, 321:640]

    def color_detect(self, left_img, right_img):
        left_hls = cv2.cvtColor(left_img, cv2.COLOR_BGR2HLS)
        right_hls = cv2.cvtColor(right_img, cv2.COLOR_BGR2HLS)
        mask_yellow = cv2.inRange(left_hls, self.YELLOW_LANE_LOW, self.YELLOW_LANE_HIGH) # 왼쪽 중앙차선 (노란색)
        mask_white = cv2.inRange(right_hls, self.WHITE_LANE_LOW, self.WHITE_LANE_HIGH) # 오른쪽 차선 (흰색)
        return mask_yellow, mask_white


if __name__ == '__main__':
    a = LaneDetection()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("program down")