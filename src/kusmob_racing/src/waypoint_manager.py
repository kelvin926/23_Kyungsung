#! /usr/bin/env python
# -*- coding:utf-8 -*-
import rospy
import csv
from visualization_msgs.msg import Marker
from move_base_msgs.msg import MoveBaseActionGoal

global counter

def callback(data):
    pos = data.goal.target_pose.pose
    print ("waypoint added {0},{1},{2},{3},").format(pos.position.x,pos.position.y,pos.orientation.z,pos.orientation.w)
    with open('waypoint.csv', 'a') as p: # csv파일에 waypoint 행을 append 함
        wr = csv.writer(p)
        wr.writerow([float(pos.position.x),float(pos.position.y),float(pos.orientation.z),float(pos.orientation.w)])
        print("{0}번째 waypoint saved {1},{2},{3},{4},").format(counter, pos.position.x,pos.position.y,pos.orientation.z,pos.orientation.w)
        make_marker(float(pos.position.x),float(pos.position.y),float(pos.orientation.z),float(pos.orientation.w))
    p.close()

rospy.init_node("waypoint_manager")

pub = rospy.Publisher("waypoint", Marker, queue_size = 10)
rospy.Subscriber("/move_base/goal", MoveBaseActionGoal, callback)

rate = rospy.Rate(250)

def make_marker(posi_x, posi_y, ori_z, ori_w):
    # Mark arrow
    global counter
    marker_data = Marker()
    marker_data.header.frame_id = "map"
    marker_data.header.stamp = rospy.Time.now()

    marker_data.ns = "basic_shapes"
    marker_data.id = counter

    marker_data.action = Marker.ADD

    marker_data.pose.position.x = posi_x
    marker_data.pose.position.y = posi_y
    marker_data.pose.position.z = 0.0

    marker_data.pose.orientation.x=0.0
    marker_data.pose.orientation.y=0.0
    marker_data.pose.orientation.z=ori_z
    marker_data.pose.orientation.w=ori_w

    marker_data.color.r = 1.0
    marker_data.color.g = 0.0
    marker_data.color.b = 0.0
    marker_data.color.a = 1.0
    marker_data.scale.x = 0.5
    marker_data.scale.y = 0.1
    marker_data.scale.z = 0.1

    marker_data.lifetime = rospy.Duration()

    marker_data.type = 0

    pub.publish(marker_data)


    # Mark num
    marker_data = Marker()
    marker_data.header.frame_id = "map"
    marker_data.header.stamp = rospy.Time.now()

    marker_data.ns = "basic_shapes"
    marker_data.id = counter

    marker_data.action = Marker.ADD

    marker_data.pose.position.x = posi_x
    marker_data.pose.position.y = posi_y
    marker_data.pose.position.z = 0.0

    marker_data.pose.orientation.x=0.0
    marker_data.pose.orientation.y=0.0
    marker_data.pose.orientation.z=ori_z
    marker_data.pose.orientation.w=ori_w

    marker_data.color.r = 0.0
    marker_data.color.g = 0.0
    marker_data.color.b = 0.0
    marker_data.color.a = 1.0
    marker_data.scale.x = 0.5
    marker_data.scale.y = 0.5
    marker_data.scale.z = 0.5

    marker_data.lifetime = rospy.Duration()

    marker_data.type = Marker.TEXT_VIEW_FACING
    marker_data.text = str(int(counter))

    pub.publish(marker_data)
    counter +=1


while not rospy.is_shutdown():
    with open('waypoint.csv', 'r') as f:
        counter = 0
        reader = csv.reader(f)
        header = next(reader)

        for row in reader:
            make_marker(map(float,row)[0], map(float,row)[1], map(float,row)[2], map(float,row)[3])

    rate.sleep()

rospy.spin()
