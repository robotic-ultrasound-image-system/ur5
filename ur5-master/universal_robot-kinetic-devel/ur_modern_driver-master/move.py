#! /usr/bin/env python
#!/usr/bin/env python
import time
import roslib; roslib.load_manifest('ur_modern_driver')
import rospy
import actionlib
from control_msgs.msg import *
from trajectory_msgs.msg import *
from sensor_msgs.msg import JointState
from math import pi

def main():
      moveit_commander.roscpp_initialize(sys.argv)
      rospy.init_node('move',annoymous=True)
      arm=moveit_commander.MoveGroupCommander('arm')
      end_effector_link=arm.get_end_effector_link()
      rospy.loginfo("the end effector link is:"+str(end_effector_link))
      arm.set_named_target("home")
      traj=arm.plan()
      arm.execute(traj)
      rospy.sleep(10)

      joint_position=[-0.0876,1.274,0.02832,0.0820,-1.273,-0.003]
      arm.set_joint_value_target(joint_position)
      arm.go()
   
      rospy.sleep(100)

      arm.remember_joint_values('saved',joint_positions)
      arm.set_named_target("up")
      arm.go()
      rospy.sleep(100)
      arm.set_named_target('saved')
      arm.go()
      rospy.sleep(1)
      arm.set_named_target("up")
      arm.go()
      moveit_commander.roscpp_shutdown()
      moveit_commander.os_exit(0)
