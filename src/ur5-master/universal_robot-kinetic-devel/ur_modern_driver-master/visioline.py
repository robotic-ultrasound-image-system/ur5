#!/usr/bin/env python
import sys
import copy
import rospy,sys
import moveit_commander
import actionlib
import roslib; roslib.load_manifest('ur_modern_driver')
import tf
from control_msgs.msg import *
from trajectory_msgs.msg import *
from sensor_msgs.msg import JointState

from geometry_msgs.msg import  PoseStamped,Pose

wpose  = geometry_msgs.msg.PoseStamped()
def listener():
   
    try:
        rospy.Subscriber("/pose_trans",PoseStamped,move_joint)  
    except KeyboardInterrupt:
        raise
    except:
        raise    


def move_joint(wpose):
    
    if (wpose.header.seq==10):
        try:
            print "============got the point "   
            moveit_commander.roscpp_initialize(sys.argv)
            arm=moveit_commander.MoveGroupCommander('manipulator')
            arm.set_goal_position_tolerance(0.01)
            arm.set_goal_orientation_tolerance(0.1)
      	    arm.set_max_velocity_scaling_factor(0.1) 
            arm.set_max_acceleration_scaling_factor(0.05) 
      #arm.set_named_target("reset")
      #$arm.go()
      #rospy.sleep(1)
      #print "============ arrival reset "  

            print "============ start  "     
            print wpose
            waypoints=[]
      #arm.set_pose_target(wpose)
            waypoints.append(arm.get_current_pose().pose)
            waypoints.append(copy.deepcopy(wpose.pose))

      ## We want the cartesian path to be interpolated at a resolution of 1 cm
      ## which is why we will specify 0.01 as the eef_step in cartesian
      ## translation.  We will specify the jump threshold as 0.0, effectively
      ## disabling it.
            (plan3, fraction) = arm.compute_cartesian_path(waypoints,0.01,0.0)
                               
            rospy.sleep(1)

            arm.execute(plan3)
                                     
            rospy.sleep(1)
  
      
      #waypoints=[]
      # start with the current pose
      #waypoints.append(arm.get_current_pose().pose)
      #waypoints.append(copy.deepcopy(wpose.pose))

      ## We want the cartesian path to be interpolated at a resolution of 1 cm
      ## which is why we will specify 0.01 as the eef_step in cartesian
      ## translation.  We will specify the jump threshold as 0.0, effectively
      ## disabling it.
      #(plan3, fraction) = arm.compute_cartesian_path(
      #                         waypoints,   # waypoints to follow
      #                        0.01,        # eef_step
      #                         0.0)         # jump_threshold
                              
            rospy.sleep(4)
            print "============ arrival goal "     
        except KeyboardInterrupt:
            raise
        except:
            raise


def main():
    try:   
	global client         
	client = actionlib.SimpleActionClient('follow_joint_trajectory', FollowJointTrajectoryAction)
        rospy.init_node("test_move", anonymous=False)
        print "Waiting for server..."
        #client.wait_for_server()
        print "Connected to server"
        inp = raw_input("Continue? y/n: ")[0]
        if (inp == 'y'):
	   listener()
           rospy.spin()
        else:
            print "Halting program"
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise
if __name__ == '__main__': main()
