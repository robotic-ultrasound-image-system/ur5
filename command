

roslaunch ur_modern_driver ur5_bringup.launch


rosrun ur_modern_driver test_move.py


 rosrun tf view_frames



cd ~/catkin_ws/src/ur_modern_driver-master/

roslaunch kinect2_bridge kinect2_bridge.launch
rosrun kinect2_viewer kinect2_viewer sd cloud

socket 192.168.1.5 29999


 roslaunch ur_gazebo ur5.launch

roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=false
roslaunch ur5_moveit_config moveit_rviz.launch config:=true


roslaunch ur5_moveit_config moveit_rviz.launch config:=true
roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch



roslaunch ur_bringup ur5_bringup.launch limited:=true robot_ip:=IP_OF_THE_ROBOT [reverse_port:=REVERSE_PORT]

roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch limited:=true

roslaunch ur5_moveit_config moveit_rviz.launch config:=true

roslaunch ur_gazebo ur5.launch





real robot:
1.roslaunch ur_modern_driver ur5_bringup.launch
2.roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=false limited:=true
3.roslaunch ur5_moveit_config moveit_rviz.launch config:=true 
存在一个错误：
bring_up:
[ INFO] [1504789648.798075878]: waitForService: Service [/kinect2/load_nodelet] is now available.
[ INFO] [1504789708.604822438]: on_goal
[ERROR] [1504789710.780998568]: Robot is protective stopped!
[ WARN] [1504789715.185140401]: Secondary port: No connection. Is controller crashed? Will try to reconnect in 10 seconds...
[ WARN] [1504789715.191573670]: Realtime port: No connection. Is controller crashed? Will try to reconnect in 10 seconds...
[ INFO] [1504789725.189786405]: Secondary port: Reconnected
[ INFO] [1504789725.192952203]: Realtime port: Reconnected
Error:   TF_NAN_INPUT: Ignoring transform for child_frame_id "tool0_controller" from authority "unknown_publisher" because of a nan value in the transform (0.000000 0.000000 0.000000) (-nan -nan -nan -nan)
         at line 244 in /tmp/binarydeb/ros-kinetic-tf2-0.5.16/src/buffer_core.cpp
Error:   TF_DENORMALIZED_QUATERNION: Ignoring transform for child_frame_id "tool0_controller" from authority "unknown_publisher" because of an invalid quaternion in the transform (-nan -nan -nan -nan)
         at line 257 in /tmp/binarydeb/ros-kinetic-tf2-0.5.16/src/buffer_core.cpp

ur5_moveit_planning_execution:
[ INFO] [1504789726.197424600]: Planning attempt 1 of at most 1
[ERROR] [1504789726.197536738]: Found empty JointState message
[ WARN] [1504789726.197600522]: Joint 'wrist_2_joint' from the starting state is outside bounds by a significant margin: [ -16.8619 ] should be in the range [ -3.14159 ], [ 3.14159 ] but the error above the ~start_state_max_bounds_error parameter (currently set to 0.1)
[ WARN] [1504789726.197624957]: Joint 'wrist_3_joint' from the starting state is outside bounds by a significant margin: [ -12.4767 ] should be in the range [ -3.14159 ], [ 3.14159 ] but the error above the ~start_state_max_bounds_error parameter (currently set to 0.1)

moveit_rviz:
[ INFO] [1504789720.683891217]: ABORTED: Solution found but controller failed during execution
[ INFO] [1504789726.220528773]: ABORTED: No motion plan found. No execution attempted.
[ERROR] [1504789730.703329743]: Ignoring transform for child_frame_id "tool0_controller" from authority "unknown_publisher" because of a nan value in the transform (0.000000 0.000000 0.000000) (-nan -nan -nan -nan)
[ERROR] [1504789730.703470849]: Ignoring transform for child_frame_id "tool0_controller" from authority "unknown_publisher" because of an invalid quaternion in the transform (-nan -nan -nan -nan)
[ERROR] [1504789733.206470083]: Ignoring transform for child_frame_id "tool0_controller" from authority "unknown_publisher" because of a nan value in the transform (-26815634996663506497926541532838688468333027731583940734935550743870004400856709289875207645414123802522204229032200024507277818670185204752351323049951232.000000 -0.000000 -26815635023192343461629092732595116300213112174903854817200734010508414678348141019230411761179382863589389466948106287263311598361505904384281637556322304.000000) (-nan -nan -nan -nan)





gazebo:
1.roslaunch ur_gazebo ur5.launch limited:=true	载入带限制的gazebo模型
2.roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true limited:=true 设置带限制路径规划仿真
3.roslaunch ur5_moveit_config moveit_rviz.launch config:=true  载入带参数的rviz路径规划。

