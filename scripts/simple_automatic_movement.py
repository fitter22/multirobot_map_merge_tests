#!/usr/bin/env python

import roslib; #roslib.load_manifest('robot_red')
import rospy
import actionlib

#move_base_msgs
from move_base_msgs.msg import *

def simple_move():

	rospy.init_node('simple_move')

	#Simple Action Client
	sac = actionlib.SimpleActionClient('turtle1/move_base', MoveBaseAction)

	#create goal
	goal = MoveBaseGoal()

	#use self?
	#set goal
	goal.target_pose.pose.position.x = 2.0
	goal.target_pose.pose.orientation.w = 1.0
	goal.target_pose.header.frame_id = 'first_move'
	goal.target_pose.header.stamp = rospy.Time.now()

	#start listner
	rospy.loginfo("Waiting for server")
	sac.wait_for_server(rospy.Duration(5))
	rospy.loginfo("Connected to the server")

	#send goal
	sac.send_goal(goal)
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
