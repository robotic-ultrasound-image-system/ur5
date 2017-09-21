#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from std_msgs.msg import String
def move_group_python_interface_tutorial():
    print "============ Starting tutorial setup"
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_group_python_interface_tutorial',
                anonymous=True)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group = moveit_commander.MoveGroupCommander("manipulator")
    display_trajectory_publisher = rospy.Publisher(
                                    '/move_group/display_planned_path',
                                    moveit_msgs.msg.DisplayTrajectory,
                                    queue_size=20)
    print "============ Waiting for RVIZ..."
    rospy.sleep(10)
    print "============ Starting tutorial "
    print "============ Reference frame: %s" % group.get_planning_frame()
    print "============ End effector: %s" % group.get_end_effector_link()
    print "============ Robot Groups:"
    print robot.get_group_names()
    print "============ Printing robot state"
    print robot.get_current_state()
    print "============"
    print "============ Generating plan 1"
    group.set_max_velocity_scaling_factor(0.2) 
    group.set_max_acceleration_scaling_factor(0.02) 
    pose_target = geometry_msgs.msg.Pose()
    pose_target.orientation.w = 1.0
    pose_target.position.x = 0.1
    pose_target.position.y = 0.20
    pose_target.position.z = 0.22
    group.set_pose_target(pose_target)
    plan1 = group.plan()


    print "============ Waiting while RVIZ displays plan1..."
    rospy.sleep(5)
    group.go(wait=True)
# Use execute instead if you would like the robot to follow
# the plan that has already been computed
    group.execute(plan1)
    group.clear_pose_targets()

    group_variable_values = group.get_current_joint_values()
    print "============ Joint values: ", group_variable_values

    group_variable_values[0] = 1
    group.set_joint_value_target(group_variable_values)

    plan2 = group.plan()

    print "============ Waiting while RVIZ displays plan2..."
    rospy.sleep(5)
    group.go(wait=True)


    waypoints = []

# start with the current pose
    waypoints.append(group.get_current_pose().pose)

# first orient gripper and move forward (+x)
    wpose = geometry_msgs.msg.Pose()
    wpose.orientation.w = 1.0
    wpose.position.x = waypoints[0].position.x + 0.1
    wpose.position.y = waypoints[0].position.y
    wpose.position.z = waypoints[0].position.z
    waypoints.append(copy.deepcopy(wpose))

# second move down
    wpose.position.z -= 0.10
    waypoints.append(copy.deepcopy(wpose))

# third move to the side
    wpose.position.y += 0.05
    waypoints.append(copy.deepcopy(wpose))
    (plan3, fraction) = group.compute_cartesian_path(
                             waypoints,   # waypoints to follow
                             0.01,        # eef_step
                             0.5)         # jump_threshold

    print "============ Waiting while RVIZ displays plan3..."
    rospy.sleep(5)

# Uncomment the line below to execute this plan on a real robot.
    group.execute(plan3)
    collision_object = moveit_msgs.msg.CollisionObject()

    moveit_commander.roscpp_shutdown()

    print "============ STOPPING"


if __name__=='__main__':
  try:
    move_group_python_interface_tutorial()
  except rospy.ROSInterruptException:
    pass

