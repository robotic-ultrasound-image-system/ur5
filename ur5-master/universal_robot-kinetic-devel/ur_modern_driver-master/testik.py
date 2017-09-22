#!/usr/bin/env python
import sys
import copy
import rospy,sys
import moveit_commander
import actionlib
import roslib; roslib.load_manifest('ur_modern_driver')
from control_msgs.msg import *
from trajectory_msgs.msg import *
from sensor_msgs.msg import JointState
from tf.transformations import euler_from_quaternion ,quaternion_from_euler
from geometry_msgs.msg import  PoseStamped,Pose
 
client = None
def move_joint():
    try:
      moveit_commander.roscpp_initialize(sys.argv)
      
      arm=moveit_commander.MoveGroupCommander('manipulator')
      
      end_effector_link=arm.get_end_effector_link()
      arm.set_goal_position_tolerance(0.01)
      arm.set_goal_orientation_tolerance(0.1)
      arm.set_max_velocity_scaling_factor(0.2) 
      arm.set_max_acceleration_scaling_factor(0.02) 
      arm.set_named_target("reset")
      arm.go()
      rospy.sleep(5)
      print "============ arrival reset "     
      
      
      
      target_pose=PoseStamped()
      target_pose.header.frame_id='world'
      target_pose.header.stamp=rospy.Time.now()
      target_pose.pose.position.x=0.22
      target_pose.pose.position.y=0.35
      target_pose.pose.position.z=0.20
      target_pose.pose.orientation.w=1.0

  
      
      arm.set_pose_target(target_pose)
      arm.set_start_state_to_current_state()
      
      traj=arm.plan()
      arm.execute(traj)
      rospy.sleep(5)
      print "============ arrival target "
      arm.set_named_target("reset")
      arm.go()
      rospy.sleep(3)
      print "============ arrival reset "     

      arm.set_max_velocity_scaling_factor(0.1) 
      arm.set_max_acceleration_scaling_factor(0.01) 
      waypoints = []

# start with the current pose
      waypoints.append(arm.get_current_pose().pose)

# first orient gripper and move forward (+x)
      wpose = geometry_msgs.msg.Pose()
      wpose.orientation.w = 1.0
      wpose.position.x = waypoints[0].position.x 
      wpose.position.y = waypoints[0].position.y
      wpose.position.z = waypoints[0].position.z+0.1
      waypoints.append(copy.deepcopy(wpose))

# second move down
      wpose.position.z += 0.10
      waypoints.append(copy.deepcopy(wpose))

# third move to the side
      wpose.position.y += 0.05
      waypoints.append(copy.deepcopy(wpose))
      (plan3, fraction) = arm.compute_cartesian_path(
                             waypoints,   # waypoints to follow
                             0.01,        # eef_step
                             0.0)         # jump_threshold
   
      arm.execute(plan3) 
      rospy.sleep(5)
      print "============ arrival waypoint "     
      arm.set_named_target("up")
      arm.go()
      rospy.sleep(1)
     
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
