#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

import math

class LidarExample():
    def __init__(self):
        # ROS part
        
        rospy.init_node("obstacle_detect")
        rospy.Subscriber("scan",LaserScan,self.scan_callback)
        self.pub_obstacle = rospy.Publisher("/lidar_obstacle",String,queue_size=1)
        self.MAX_ANGLE_DEG = 90
        self.MIN_ANGLE_DEG = -90
        self.MAX_OBST_ANGLE_DEG = 10
        self.MIN_OBST_ANGLE_DEG = -10

# ==================================================
#                 Callback Functions
# ==================================================
    def scan_callback(self, data):
        for i,n in enumerate(data.ranges):
            angle = data.angle_min + data.angle_increment * i
            angle_deg = angle * 180 / math.pi
            
            x = n * math.cos(angle)
            y = n * math.sin(angle)
            
            if angle_deg < self.MAX_ANGLE_DEG and angle_deg > self.MIN_ANGLE_DEG and not n == 0:
                print("lidar angle and range : ({},{})".format(angle, n))
                print("lidar x and y : ({},{})".format(x, y))
            if angle_deg < self.MAX_OBST_ANGLE_DEG and angle_deg > self.MIN_OBST_ANGLE_DEG:
                if n < 0.25:
                    self.pub_obstacle.publish("obstacle")
                else:
                    self.pub_obstacle.publish("nothing")

def run():
    new_class = LidarExample()
    rospy.loginfo_once("ROS Node Initialized")
    rospy.spin()
            
if __name__=="__main__":
    run()
