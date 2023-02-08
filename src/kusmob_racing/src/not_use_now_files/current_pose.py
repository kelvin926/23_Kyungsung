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
        rospy.init_node('kusmob_navigation', anonymous=False)
        self.drive_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1) # limo_base에게 계산된 조향값 전달
        rospy.Subscriber("/lane/left_lane_x", Int32, self.left_lane_cb)
        rospy.Subscriber("/lane/right_lane_x", Int32, self.right_lane_cb)
        rospy.Timer(rospy.Duration(0.03), self.total_drive_control) # 0.03초마다 drive_control 함수를 실행



#################### 메인 함수 ####################
if __name__ == '__main__':

    MoveCar = kusmob_car()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("program down")