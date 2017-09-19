#!/usr/bin/env python
import rospy,sys
import moveit_commander
import actionlib
import roslib; roslib.load_manifest('ur_modern_driver')
from control_msgs.msg import *
from trajectory_msgs.msg import *
from sensor_msgs.msg import JointState


client = None
def move_joint():
    try:
      moveit_commander.roscpp_initialize(sys.argv)
      arm=moveit_commander.MoveGroupCommander('manipulator')
      end_effector_link=arm.get_end_effector_link()
      rospy.loginfo("the end effector link is:"+str(end_effector_link))
      arm.set_named_target("home")
      traj=arm.plan()
      arm.execute(traj)
      rospy.sleep(5)

      joint_position=[1.3,-0.30,0,0,0,0]
      arm.set_joint_value_target(joint_position)
      arm.go()
   
      rospy.sleep(5)

      arm.remember_joint_values('saved',joint_position)
      arm.set_named_target("reset")
      arm.go()
      rospy.sleep(5)
      arm.set_named_target('saved')
      arm.go()
      rospy.sleep(5)
      arm.set_named_target("reset")
      arm.go()
      moveit_commander.roscpp_shutdown()
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
        inp = raw_input("Continue? y/n: ")[0]
        if (inp == 'y'):
            move_joint()
        else:
            print "Halting program"
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise

if __name__ == '__main__': main()
