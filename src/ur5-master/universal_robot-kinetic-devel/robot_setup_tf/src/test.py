#! /usr/bin/python

# ***********************************************************
PKG = 'ur_modern_driver'
import sys
import rospy
import sys
import copy
import rospy, sys
import moveit_commander
import actionlib
import roslib;

roslib.load_manifest('ur_modern_driver')
import tf
from control_msgs.msg import *
from trajectory_msgs.msg import *
from sensor_msgs.msg import JointState

from geometry_msgs.msg import PoseStamped, Pose, PointStamped


def main():
    try:
        rospy.init_node("pose_drawer", anonymous=False)
        Pose_Drawer
        ros.spin()
    except KeyboardInterrupt:
        raise


if __name__ == '__main__': main()
