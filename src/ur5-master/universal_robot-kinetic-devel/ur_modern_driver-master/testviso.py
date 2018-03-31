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

from geometry_msgs.msg import  PoseStamped,Pose,PointStamped


wpoint = geometry_msgs.msg.PoseStamped()
wpose  = geometry_msgs.msg.PoseStamped()
def listener():
   
    try:
        rospy.Subscriber("/pose_trans",PoseStamped,move_joint)  
    except KeyboardInterrupt:
        raise
    except:
        raise
def move_joint(wpoint):
    try:
      print "============got the point "   
      moveit_commander.roscpp_initialize(sys.argv)
      arm=moveit_commander.MoveGroupCommander('manipulator')
      arm.set_goal_position_tolerance(0.001)
      arm.set_goal_orientation_tolerance(0.001)
      arm.set_max_velocity_scaling_factor(0.1) 
      arm.set_max_acceleration_scaling_factor(0.05) 
      #$arm.go()
      #rospy.sleep(1)
      #print "============ arrival reset "  

      end_effector_link=arm.get_end_effector_link()
      target_pose= geometry_msgs.msg.PoseStamped()
      saved_target_pose= geometry_msgs.msg.PoseStamped()



      
      arm.set_start_state_to_current_state()

      target_pose=arm.get_current_pose(end_effector_link)
      saved_target_pose=arm.get_current_pose(end_effector_link)


      target_pose.pose.position.x=wpoint.pose.position.x
      target_pose.pose.position.y=wpoint.pose.position.y
      target_pose.pose.position.z=wpoint.pose.position.z+0.092+0.05
      
      arm.set_pose_target(target_pose,end_effector_link)
      print target_pose
      traj=arm.plan()
      arm.execute(traj)
      
      rospy.sleep(2)
      arm.set_start_state_to_current_state()
      arm.set_pose_target(saved_target_pose,end_effector_link)
      traj=arm.plan()
      arm.execute(traj)
      rospy.sleep(2)
      
  
    
      #waypoints=[]
      #arm.set_pose_target(wpose)
      #waypoints.append(arm.get_current_pose().pose)
      #waypoints.append(copy.deepcopy(wpose.pose))

      ## We want the cartesian path to be interpolated at a resolution of 1 cm
      ## which is why we will specify 0.01 as the eef_step in cartesian
      ## translation.  We will specify the jump threshold as 0.0, effectively
      ## disabling it.
      #(plan3, fraction) = arm.compute_cartesian_path(
      #                         waypoints,   # waypoints to follow
      #                         0.01,        # eef_step
      #                         0.0)         # jump_threshold
                               
      #rospy.sleep(1)

      #arm.execute(plan3)
                                     
      #
      #rospy.sleep(1)
  
      
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
