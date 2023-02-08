#!/usr/bin/env python
# -*- coding:utf-8 -*-
import rospy
import actionlib
import tf
from nav_msgs.msg import Odometry
import math
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import csv


def goal_pose(pose): 
    goal_pose = MoveBaseGoal()
    goal_pose.target_pose.header.frame_id = 'map'
    goal_pose.target_pose.pose.position.x = map(float,pose)[0]
    goal_pose.target_pose.pose.position.y = map(float,pose)[1]
    goal_pose.target_pose.pose.position.z = 0.0
    goal_pose.target_pose.pose.orientation.x = 0.0
    goal_pose.target_pose.pose.orientation.y = 0.0
    goal_pose.target_pose.pose.orientation.z = map(float,pose)[2]
    goal_pose.target_pose.pose.orientation.w = map(float,pose)[3]

    return goal_pose


if __name__ == '__main__':
    rospy.init_node('waypoint_move')
    listener = tf.TransformListener()

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction) 
    client.wait_for_server()
    listener.waitForTransform("map", "base_link", rospy.Time(), rospy.Duration(4.0))

    while True:
        with open('waypoint.csv', 'r') as f: # waypoint.csv파일을 읽어온다
            counter = 0
            reader = csv.reader(f)
            header = next(reader)

            for pose in reader:
                goal = goal_pose(pose)
                client.send_goal(goal)
                while True:
                    now = rospy.Time.now()
                    listener.waitForTransform("map", "base_link", now, rospy.Duration(4.0))

                    # map좌표계의 현재 위치를 tf에서 받는다
                    position, quaternion = listener.lookupTransform("map", "base_link", now)

                    # 웨이 포인트의 골 주위 0.3m이내에 로봇이 오면 다음 웨이 포인트를 발행하는
                    if(math.sqrt((position[0]-goal.target_pose.pose.position.x)**2 + (position[1]-goal.target_pose.pose.position.y)**2 ) <= 0.3):
                        counter += 1
                        print("Arrived, We go {} Waypoint").format(counter)
                        break

                    else:
                        rospy.sleep(0.5)