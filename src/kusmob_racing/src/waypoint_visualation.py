import rospy
import csv
from visualization_msgs.msg import Marker

rospy.init_node("waypoint_visualation")

pub = rospy.Publisher("waypoint", Marker, queue_size = 10)

rate = rospy.Rate(25)


while not rospy.is_shutdown():
    way_point_data = list()
    with open('waypoint.csv', 'r') as f: # waypoint.csv 파일을 읽어와서 리스트에 저장
        counter = 0
        while True:
            line = f.readline().rstrip("\n")
            if line:
                line = line.split(",")
                way_point_data.append(line)
            else:
                way_point_data.pop(0)
                f.close()
                break

        for row in way_point_data:
            # Mark arrow
            marker_data = Marker()
            marker_data.header.frame_id = "map"
            marker_data.header.stamp = rospy.Time.now()

            marker_data.ns = "basic_shapes"
            marker_data.id = counter

            marker_data.action = Marker.ADD

            marker_data.pose.position.x = map(float,row)[0]
            marker_data.pose.position.y = map(float,row)[1]
            marker_data.pose.position.z = 0.0

            marker_data.pose.orientation.x=0.0
            marker_data.pose.orientation.y=0.0
            marker_data.pose.orientation.z=map(float,row)[2]
            marker_data.pose.orientation.w=map(float,row)[3]

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
            counter +=1


            # Mark num
            marker_data = Marker()
            marker_data.header.frame_id = "map"
            marker_data.header.stamp = rospy.Time.now()

            marker_data.ns = "basic_shapes"
            marker_data.id = counter

            marker_data.action = Marker.ADD

            marker_data.pose.position.x = map(float,row)[1]
            marker_data.pose.position.y = map(float,row)[2]
            marker_data.pose.position.z = map(float,row)[3]

            marker_data.pose.orientation.x=map(float,row)[4]
            marker_data.pose.orientation.y=map(float,row)[5]
            marker_data.pose.orientation.z=map(float,row)[6]
            marker_data.pose.orientation.w=map(float,row)[7]

            marker_data.color.r = 0.0
            marker_data.color.g = 0.0
            marker_data.color.b = 0.0
            marker_data.color.a = 1.0
            marker_data.scale.x = 0.5
            marker_data.scale.y = 0.5
            marker_data.scale.z = 0.5

            marker_data.lifetime = rospy.Duration()

            marker_data.type = Marker.TEXT_VIEW_FACING
            marker_data.text = str(int(map(float,row)[0]))

            pub.publish(marker_data)
            counter +=1

    rate.sleep()

rospy.spin()
