#!/usr/bin/env python
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
      rospy.sleep(2)
      
      
   
      

      target_pose.pose.position.x=-0.62
      target_pose.pose.position.y=-0.35
      target_pose.pose.position.z=0.20
      target_pose.pose.orientation.w=1.0

  
      
      arm.set_pose_target(target_pose,end_effector_link)
      arm.set_start_state_to_current_state()
      
      traj=arm.plan()
      arm.execute(traj)
      rospy.sleep(2)
     


      saved_target_pose=arm.get_current_pose(end_effector_link)
      arm.set_named_target("reset")
      arm.go()
      rospy.sleep(1)
      
      arm.set_pose_target(saved_target_pose,end_effector_link)
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
