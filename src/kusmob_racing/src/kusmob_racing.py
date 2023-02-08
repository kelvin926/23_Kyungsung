#!/usr/bin/env python
# -*- coding:utf-8 -*-
import rospy
import math
import cv2
import numpy as np
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from std_msgs.msg import Int32 ,String
from cv_bridge import CvBridge


class kusmob_car:
    def __init__(self):
        rospy.init_node("kusmob_car")
        self.BASE_SPEED = 0.2 # 0.2 (m/s)
        self.LANE_LATERAL_GAIN = 0.005 # 0.005 (라인트레이싱의 조향축 가중치 값)
        self.WAYPOINY_LATERAL_GAIN = 0.005 # 0.005 (웨이포인트의 조향축 가중치 값)
        self.drive_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1) # limo_base에게 계산된 조향값 전달
        rospy.Subscriber("/lane/delta_lane_x", Int32, self.lane_drive_control) # 라인트레이싱의 조향값을 받음
        self.with_lane_control = True # 라인트레이싱을 통해 주행할지 여부 (기본 값 : True)
        self.with_waypoint_control = True # 웨이포인트를 통해 주행할지 여부 (기본 값 : True)
        rospy.Timer(rospy.Duration(0.03), self.total_drive_control) # 0.03초마다 drive_control 함수를 실행


#################### 라인트레이싱 관련 함수 ####################

    def lane_drive_control(self, lane_x):
        try:
            self.lane_off_center = lane_x
            rospy.loginfo("lane_off_center = {}".format(self.lane_off_center))
            self.lane_drive = Twist()
            self.lane_drive.linear.x = self.BASE_SPEED
            self.lane_drive.angular.z = self.lane_off_center * self.LATERAL_GAIN
            # self.drive_pub.publish(lane_drive)
        except:
            pass

#################### 웨이포인트 관련 함수 ####################
    def waypoint_drive_control(self, event):
        try:
            pass
        except:
            pass


#################### 주행 관련 함수 ####################
    def total_drive_control(self, event):
        if self.with_lane_control == True:
            self.lane_drive_control(event)
        else:
            pass

        if self.with_waypoint_control == True:
            self.waypoint_drive_control(event)
        else:
            pass



#################### 메인 함수 ####################
if __name__ == '__main__':
    Start_num = input("Speed Racing이면 1, Mission Racing이면 2를 입력하세요. TEST면 0을 입력하세요:")
    if Start_num == 1: # Speed Racing
        print("Speed Racing을 시작합니다.")
    elif Start_num == 2: # Mission Racing
        print("Mission Racing을 시작합니다.")
    elif Start_num == 0: # TEST
        print("TEST를 시작합니다.")
    else:
        print("잘못된 입력입니다. 즉시 프로그램을 종료해주세요. (ctrl + c)")
    
    MoveCar = kusmob_car()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("program down")