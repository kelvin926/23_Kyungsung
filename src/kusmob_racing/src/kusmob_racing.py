#!/usr/bin/env python
# -*- coding:utf-8 -*-
import rospy
import math
import cv2
import numpy as np
import actionlib
import tf
import csv
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from std_msgs.msg import Int32 ,String
from cv_bridge import CvBridge
from nav_msgs.msg import Odometry, Int32
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseActionGoal

'''
self.lane_drive.linear.x : 라인트레이싱의 속도
self.lane_drive.angular.z : 라인트레이싱으로 얻은 조향 값
self.now_traffic_light : 현재 신호등 상태
self.waypoint_num : 현재 Waypoint 넘버
'''



class kusmob_car:
    def __init__(self):
        rospy.init_node("kusmob_car")

        self.BASE_SPEED = 0.2 # 0.2 (m/s)
        self.LANE_LATERAL_GAIN = 0.005 # 0.005 (라인트레이싱의 조향축 가중치 값)
        self.WAYPOINT_LATERAL_GAIN = 0.005 # 0.005 (웨이포인트의 조향축 가중치 값)

        self.drive_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1) # limo_base에게 계산된 조향값 전달

        rospy.Subscriber("/lane/delta_lane_x", Int32, self.now_lane_x) # 라인트레이싱의 조향값을 받음
        rospy.Subscriber("/traffic_light", String, self.traffic_light) # 신호등의 상태를 받음
        rospy.Subscriber("/now_waypoint", Int32, self.now_waypoint) # 웨이포인트의 값을 받음

        rospy.Timer(rospy.Duration(0.03), self.how_drive) # 0.03초마다 how_drive 함수 실행

        self.want_waypoint_num = rospy.Publisher("/want_waypoint_num", Int32, queue_size=1) # waypoint_move에게 웨이포인트를 전달
        
        self.way_point_data = list()
        with open('waypoint.csv', 'r') as f: # waypoint.csv 파일을 읽어와서 리스트에 저장
            while True:
                line = f.readline().rstrip("\n")
                if line:
                    line = line.split(",")
                    self.way_point_data.append(line)
                else:
                    self.way_point_data.pop(0)
                    f.close()
                    break


#################### 라인트레이싱 관련 함수 ####################

    def now_lane_x(self, now_lane_x):
        self.lane_center = now_lane_x

    def lane_drive_control(self, now_lane_x):
        rospy.loginfo("lane_center = {}".format(self.lane_center))
        self.lane_drive = Twist()
        self.lane_drive.linear.x = self.BASE_SPEED # 라인트레이싱 속도 ********************
        self.lane_drive.angular.z = now_lane_x * self.LATERAL_GAIN # 라인트레이싱으로 얻은 조향값 ********************
        return self.lane_drive

#################### 웨이포인트 관련 함수 ####################
    def now_waypoint(self, waypoint_num): # waypoint_move에게서 받은 현재 Waypoint 값을 넣음
        self.now_waypoint_num = waypoint_num

    def waypoint_drive_control(self, want_waypoint_num):
        self.want_waypoint_num.publish(want_waypoint_num) # 목표 좌표를 waypoint_move에게 전달


################ 신호등 관련 함수 ################
    def traffic_light(self, traffic_light):
        try:
            if traffic_light == "red":
                self.now_traffic_light = "red"
            elif traffic_light == "green":
                self.now_traffic_light = "green"
            elif traffic_light == "blue":
                self.now_traffic_light = "blue"
            else:
                self.now_traffic_light = "none"
        except:
            pass


#################### 주행 관련 함수 ####################
    def total_drive_control(self, waypoint=True, lane_control=True, want_waypoint_num=0):
        # if (self.waypoint == True) and (self.with_lane_control == True):
        #     pass # 둘 다 사용할 경우
        # else:
        #     pass
        if (waypoint == True) and (lane_control == False):
            # 웨이포인트만 사용할 경우
            self.waypoint_drive_control(want_waypoint_num)
        else:
            pass
        if (self.waypoint == False) and (lane_control == True):
            # 라인트레이싱만 사용할 경우
            self.drive_pub.publish(self.lane_drive_control(self.lane_center))
        else:
            pass

    def how_drive(self, event):
        if self.now_traffic_light == "red":
            self.total_drive_control(waypoint=False, lane_control=True, want_waypoint_num=0)
        if self.now_traffic_light == "green":
            self.total_drive_control(waypoint=True, lane_control=False, want_waypoint_num=1)
        



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
        while True:
            MoveCar.how_drive(True)
    except KeyboardInterrupt:
        print("program down")