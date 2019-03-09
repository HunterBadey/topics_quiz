#! /usr/bin/env python

# import libraries
import rospy
import math
# from geometry_msg import velocities
from geometry_msgs.msg import Twist
# from sensor_msg import ranges
from sensor_msgs.msg import LaserScan


velocity = Twist()
velocity.linear.x = 1
velocity.angular.z = 0
velocity.linear.y = 0

rospy.init_node('topics_quiz_node')


def callback(msg):
    # print msg.ranges[360]
    pub.publish(velocity)
    if msg.ranges[360] <= 2:
        velocity.linear.x = 0
        velocity.angular.z = - math.pi
        pub.publish(velocity)


pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
rospy.spin()
