#!/usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
from std_msgs.msg import String
import math
from geometry_msgs.msg import Twist

class move_limo:
    def __init__(self):
        rospy.init_node('mission_control')

        self.BASE_SPEED = 0.2


        self.obstacle = rospy.Subscriber("/lidar_obstacle", String, self.detect_obstacle)

        self.drive_pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)

        rospy.Timer(rospy.Duration(0.03), self.mission_control)


    def mission_control(self, event):

            try:

                drive = Twist()
                if self.obstacle_detect:
                    drive.linear.x = 0.0
                    drive.angular.z = 0.0
                    #print('stop')
                else:
                    drive.linear.x = self.BASE_SPEED
                    drive.angular.z = 0.0
                    #print('go')

                self.drive_pub.publish(drive)
                
            except:
                pass 
                

    def detect_obstacle(self, data):
        if data.data == "obstacle":
            self.obstacle_detect = True
        else:
            self.obstacle_detect = False
        print(self.obstacle_detect)
        
            



if __name__ == '__main__':
    MoveCar = move_limo()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("program down")
