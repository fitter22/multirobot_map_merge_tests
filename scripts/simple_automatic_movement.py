#!/usr/bin/env python

import roslib; #roslib.load_manifest('robot_red')
import rospy
import actionlib

#move_base_msgs
from move_base_msgs.msg import *
#from geometry_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def simple_move():

	rospy.init_node('simple_move')

	#Simple Action Client
	sac = actionlib.SimpleActionClient('move_base', MoveBaseAction)

	#pub = rospy.Publisher("turtle1/move_base/goal", PoseStamped, queue_size = 10)

	#create goal
	goal = MoveBaseGoal()
	#goal = PoseStamped()

	#set goal
	goal.target_pose.pose.position.x = 1.0
	#goal.target_pose.pose.orientation.w = 1.0
	goal.target_pose.header.frame_id = 'odom'
	goal.target_pose.header.stamp = rospy.Time.now()

	#goal.header.frame_id = 'base_link'
	#goal.pose.position.x = 2.0
	#goal.pose.orientation.w = 1.0
	#goal.header.stamp = rospy.Time.now()

	#start listner
	rospy.loginfo("Waiting for server")
	sac.wait_for_server(rospy.Duration(5))
	rospy.loginfo("Connected to the server")

	#send goal
	sac.send_goal(goal)
	#pub.publish(goal)
	rospy.loginfo("Goal sent")

	#finish
	sac.wait_for_result()

	#print result
	print sac.get_result()


if __name__ == '__main__':
	try:
		simple_move()
	except rospy.ROSInterruptException:
		print "Keyboard Interrupt"
