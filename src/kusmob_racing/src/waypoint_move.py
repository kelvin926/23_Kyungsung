#!/usr/bin/env python
# -*- coding:utf-8 -*-
import rospy
import actionlib
import tf
from nav_msgs.msg import Odometry, Int32
import math
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseActionGoal
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

def make_temp_waypoint(input_waypoint):
    global temp_waypoint
    if temp_waypoint == input_waypoint:
        pass
    else:
        temp_waypoint = input_waypoint

def call_back(want_waypoint_num):
    global way_num
    way_num = want_waypoint_num
    make_temp_waypoint(want_waypoint_num)
    global want_waypoint_xyz
    want_waypoint_xyz = way_point_data[want_waypoint_num]


if __name__ == '__main__':
    temp_waypoint = 0
    way_point_data = list()
    with open('waypoint.csv', 'r') as f: # waypoint.csv 파일을 읽어와서 리스트에 저장
        while True:
            line = f.readline().rstrip("\n")
            if line:
                line = line.split(",")
                way_point_data.append(line)
            else:
                way_point_data.pop(0)
                f.close()
                break

    rospy.init_node('waypoint_move')
    listener = tf.TransformListener()

    now_waypoint = rospy.Publisher("/now_waypoint", Int32, queue_size=1) # kusmob_racing에게 현재 웨이포인트를 알려준다
    rospy.Subscriber("/want_waypoint_num", Int32, call_back) # 원하는 웨이포인트를 받는다

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction) 
    client.wait_for_server()
    listener.waitForTransform("map", "base_link", rospy.Time(), rospy.Duration(4.0))


    while True:
        while (temp_waypoint != way_num): # 받은 웨이포인트가 다를 때 실행
            goal = goal_pose(want_waypoint_xyz)
            now = rospy.Time.now()
            listener.waitForTransform("map", "base_link", now, rospy.Duration(4.0))

            # map좌표계의 현재 위치를 tf에서 받는다
            position, quaternion = listener.lookupTransform("map", "base_link", now)
            # 웨이 포인트의 골 주위 0.3m이내에 로봇이 오면 다음 웨이 포인트를 발행하는
            client.send_goal(goal)
            if(math.sqrt((position[0]-goal.target_pose.pose.position.x)**2 + (position[1]-goal.target_pose.pose.position.y)**2 ) <= 0.3):
                now_waypoint.publish(int(way_num)) # 현재 waypoint 발행
                print("Arrived at {}").format(way_num)
                break

            else:
                pass
                # rospy.sleep(0.5)