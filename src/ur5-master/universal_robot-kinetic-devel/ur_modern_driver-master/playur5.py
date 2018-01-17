#!/usr/bin/env python
import sys
import copy
import rospy,sys
import moveit_commander
import actionlib
import roslib; roslib.load_manifest('ur_modern_driver')

from control_msgs.msg import *
from trajectory_msgs.msg import *
from sensor_msgs.msg import JointState,Joy
from geometry_msgs.msg import  PoseStamped,Pose,PointStamped

jpose  = Joy()
def listener():
   
    try:
        rospy.Subscriber("/joy",Joy,move_joint)  
    except KeyboardInterrupt:
        raise
    except:
        raise
def move_joint(jpose):
    try:
      #print "============got the point " 
      #print jpose.buttons  
      if (jpose.buttons[0]):
          print "left"
          #jpose.buttons[0]=0
      if (jpose.buttons[1]):
          print "right"
	  #jpose.buttons[1]=0
      if (jpose.buttons[2]):
          print "forword"
	  #jpose.buttons[2]=0
      if (jpose.buttons[3]):
          print "backword"
	  #jpose.buttons[3]=0
      if (jpose.buttons[4]):
          print "up"
	  #jpose.buttons[4]=0
      if (jpose.buttons[5]):
          print "down"      
	  #jpose.buttons[5]=0
      #arm.set_named_target("reset")
      #$arm.go()
      #rospy.sleep(1)
      #print "============ arrival reset "  

      #print "============ start  "     
      #wpose.header=wpoint.header
      #wpose.pose.position=wpoint.point
      #print wpose
      

  
      
  
    
      #waypoints=[]
      #arm.set_pose_target(wpose)
      #waypoints.append(arm.get_current_pose().pose)
      #waypoints.append(copy.deepcopy(wpose.pose))

      ## We want the cartesian path to be interpolated at a resolution of 1 cm
      ## which is why we will specify 0.01 as the eef_step in cartesian
      ## translation.  We will specify the jump threshold as 0.0, effectively
      ## disabling it.
      #(plan3, fraction) = arm.compute_cartesian_path(
                               #waypoints,   # waypoints to follow
                               #0.01,        # eef_step
                               #0.0)         # jump_threshold
                               
      #rospy.sleep(1)

      #arm.execute(plan3)
                                     
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
                              
      #rospy.sleep(4)
      #print "============ arrival goal "     
    except KeyboardInterrupt:
        raise
    except:
        raise
def left():
    
    





def main():
    try:   
	global client         
	client = actionlib.SimpleActionClient('follow_joint_trajectory', FollowJointTrajectoryAction)
        rospy.init_node("joy_move", anonymous=False)
        moveit_commander.roscpp_initialize(sys.argv)
        arm=moveit_commander.MoveGroupCommander('manipulator')
        arm.set_goal_position_tolerance(0.01)
        arm.set_goal_orientation_tolerance(0.1)
        arm.set_max_velocity_scaling_factor(0.1) 
        arm.set_max_acceleration_scaling_factor(0.05) 
        print "Waiting for server..."
        client.wait_for_server()
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
