#! /usr/bin/env python3


import rospy
from geometry_msgs.msg import PoseStamped

rospy.init_node('set_init_pose')
pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)

goal= PoseStamped()
goal.header.frame_id= 'map'

goal.pose.position.x=2.0
goal.pose.position.y= 0.0
goal.pose.position.z= 0.0

goal.pose.orientation.x= 0.0
goal.pose.orientation.y= 0.0
goal.pose.orientation.z= 0.0
goal.pose.orientation.w= 1.0
rospy.sleep(1)

pub.publish(goal)
