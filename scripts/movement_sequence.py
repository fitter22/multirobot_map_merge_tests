#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class Sequence_move():
    def __init__(self):
        rospy.init_node('sequence_move', anonymous = False)

        rospy.loginfo("Seqence started, CTRL-C to abort")
        rospy.on_shutdown(self.shutdown)

        self.turtle1_vel = rospy.Publisher('turtle1/cmd_vel_mux/input/navi', Twist, queue_size=10)
        self.turtle2_vel = rospy.Publisher('turtle2/cmd_vel_mux/input/navi', Twist, queue_size=10)

        # move command update rate (Hz)
        r = rospy.Rate(10);

        turtle1_cmd = Twist()
	    # go forward at 0.2 m/s
        turtle1_cmd.linear.x = 0.2
	    # turn at 0.2 radians/s
        turtle1_cmd.angular.z = 0.2

        turtle2_cmd = Twist()
        turtle2_cmd.linear.x = 0.5
        turtle2_cmd.angular.z = 0.077

        # publish move command until CTRL-C
        while not rospy.is_shutdown():
            self.turtle1_vel.publish(turtle1_cmd)
            self.turtle2_vel.publish(turtle2_cmd)
            r.sleep()

    def shutdown(self):
        rospy.loginfo("Stop TurtleBot")
        # a default Twist has linear.x of 0 and angular.z of 0. So it'll stop TurtleBot
        self.turtle1_vel.publish(Twist())
        # sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
        rospy.sleep(1)


if __name__ == '__main__':
	try:
		Sequence_move()
	except:
		rospy.loginfo("Sequence terminated")
