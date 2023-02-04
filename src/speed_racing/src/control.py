#!/usr/bin/env python
# -*- coding:utf-8 -*-
## lane_detection/scripts/control_wecar.py
import rospy
from std_msgs.msg import Int32, String
import math
from geometry_msgs.msg import Twist

class move_limo:
    def __init__(self):
        rospy.init_node('control', anonymous=True)
        self.ref_x = 180
        self.ref_dist_to_left = 140
        self.BASE_SPEED = 0.2
        self.LATERAL_GAIN = 0.1


        self.traffic_light_last_time = rospy.Time.now().to_sec()

        self.left_lane_x = rospy.Subscriber("/lane/left_lane_x", Int32, self.lane_cb)

        self.drive_pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)

        rospy.Timer(rospy.Duration(0.03), self.drive_control)


    def drive_control(self, event):

            try:
                self.off_center = -(self.left_x + self.ref_x - 320.0)
                rospy.loginfo("off_center, lateral_gain = {}, {}".format(self.off_center, self.LATERAL_GAIN))
                drive = Twist()
                drive.linear.x = self.BASE_SPEED
                drive.angular.z = self.off_center * self.LATERAL_GAIN
                self.drive_pub.publish(drive)
                
            except:
                pass 
                

    def lane_cb(self, data):
        if data.data == -1:
            self.left_x = 0
        else:
            self.left_x = data.data 
            



if __name__ == '__main__':
    MoveCar = move_limo()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("program down")
