#!/usr/bin/env python
import time
import roslib;

roslib.load_manifest('ur_modern_driver')
import rospy
import actionlib
from control_msgs.msg import *
from trajectory_msgs.msg import *
from sensor_msgs.msg import JointState
from math import pi

JOINT_NAMES = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint',
               'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']

Q1 = [2.2, 0, -1.57, 0, 0, 0]
Q2 = [1.5, 0, -1.57, 0, 0, 0]

client = None


def move_repeated():
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES
    try:
        joint_states = rospy.wait_for_message("joint_states", JointState)
        joints_pos = joint_states.position
        d = 5.0
        g.trajectory.points = [
            JointTrajectoryPoint(positions=joints_pos, velocities=[0] * 6, time_from_start=rospy.Duration(0.0))]
        for i in range(20):
            g.trajectory.points.append(
                JointTrajectoryPoint(positions=Q1, velocities=[0] * 6, time_from_start=rospy.Duration(d)))
            d += 2
            g.trajectory.points.append(
                JointTrajectoryPoint(positions=Q2, velocities=[0] * 6, time_from_start=rospy.Duration(d)))
            d += 2
        client.send_goal(g)
        client.wait_for_result()
    except KeyboardInterrupt:
        client.cancel_goal()
        raise
    except:
        raise


def main():
    global client
    try:
        rospy.init_node("test_move", anonymous=True, disable_signals=True)

        client = actionlib.SimpleActionClient('follow_joint_trajectory', FollowJointTrajectoryAction)
        print "Waiting for server..."
        client.wait_for_server()
        print "Connected to server"
        parameters = rospy.get_param(None)
        index = str(parameters).find('prefix')
        if (index > 0):
            prefix = str(parameters)[index + len("prefix': '"):(
                index + len("prefix': '") + str(parameters)[index + len("prefix': '"):-1].find("'"))]
            for i, name in enumerate(JOINT_NAMES):
                JOINT_NAMES[i] = prefix + name
        print "This program makes the robot move between the following three poses:"
        print str([Q1[i] * 180. / pi for i in xrange(0, 6)])
        print str([Q2[i] * 180. / pi for i in xrange(0, 6)])
        print "Please make sure that your robot can move freely between these poses before proceeding!"
        inp = raw_input("Continue? y/n: ")[0]
        if (inp == 'y'):
            # move1()
            move_repeated()
            # move_disordered()
            # move_interrupt()
        else:
            print "Halting program"
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise


if __name__ == '__main__': main()
