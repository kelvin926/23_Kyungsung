#!/usr/bin/env python
# -*- coding:utf-8 -*-
import rospy
from std_msgs.msg import Int32, String
import math
from geometry_msgs.msg import Twist

class move_limo:
    def __init__(self):
        rospy.init_node('control', anonymous=True)
        self.ref_x = 320
        self.BASE_SPEED = 0.2
        self.LATERAL_GAIN = 0.1 # 가중치


        # self.traffic_light_last_time = rospy.Time.now().to_sec()

        self.left_x = rospy.Subscriber("/lane/left_lane_x", Int32, self.lane_cb)
        self.right_x = rospy.Subscriber("/lane/right_lane_x", Int32, self.lane_cb)

        self.drive_pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)

        rospy.Timer(rospy.Duration(0.03), self.drive_control)


    def drive_control(self, event):

# 센터의 x좌표 값은 320이다.
            try:
                self.off_center = (self.left_x + self.right_x) / 2 - self.ref_x
                rospy.loginfo("off_center, lateral_gain = {}, {}".format(self.off_center, self.LATERAL_GAIN))
                drive = Twist()
                drive.linear.x = self.BASE_SPEED
                drive.angular.z = self.off_center * self.LATERAL_GAIN
                self.drive_pub.publish(drive)
                
            except:
                pass 
                

    def lane_cb(self, data):
        if data.data == -1:
            return 0
        else:
            return data.data 
            


if __name__ == '__main__':
    MoveCar = move_limo()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("program down")
