日志文件
===================================  
十分重要  
-----------------------------------
## Author:Lirui  
## E-mail:lirui2017@email.szu.edu.cn  

-----------------------------------

##### This file would be used to record the commands history ordered by dates  
##### rules:
           * date for Contenys
           * cutting line: --------
           * codes for table key
           * #focus#
           * record steps
           * link the source web

----------------------------------
# Contents
 * [2017-8-31](#2017-8-31)
 * [2017-9-3](#2017-9-3)
 * [2017-9-4](#2017-9-4)
 * [2017-9-6](#2017-9-6)
 * [2017-9-7](#2017-9-7)
 * [2017-9-8](#2017-9-8)
 * [2017-9-9](#2017-9-9)
 * [2017-9-10](#2017-9-10)
 * [2017-9-11](#2017-9-11)
 * [2017-9-12](#2017-9-12)
 * [2017-9-18](#2017-9-18)
 * [2017-9-19](#2017-9-19)
----------------------------------
# 2017-8-31
----------------------------------
	there is something wrong.
	this package is not support with anything over 1.9.x.
	since the ur_driver is, AFAIK, not compatible with UR v3.X.	
	but do not delete this folder.

[source](https://github.com/ros-industrial/universal_robot)

--------------------------------
	if you want to go ahead ,please just download the  ur_modern_driver.
	I will test the package above.
[source](https://github.com/ThomasTimm/ur_modern_driver)
--------------------------------
	I have already tried it,but this package can't world correctly.
	I will find a new one.
	This web published one metheod. I will try it.
	yes. I compile the package successfull.
[source](http://www.linuxidc.com/Linux/2017-03/141507.htm)  

### **Follow this steps**   
	1.download universal_robot_kinetic_devel into the catkin_ws/src
	2.dowload  ur_modern_driver_master  into the file above to take the place of ur_driver
	3.change the  ur_hardware_interface.cpp  with the codes in the  [web](http://www.linuxidc.com/Linux/2017-03/141507.htm "blogs")
  	4:catkin_make
-------------------------------
	It's  apparently that  that way can't work.
	I will try a new one.
	##~~https://github.com/VCBE123/ur_modern_driver~~##      
	this is my own page.
	there is something wrong .
        I do it once again.
------------------------------
*Successsfull*  

************************************************* **github** *******************  

	1.install git 

		$ git
		The program 'git' is currently not installed. You can install it by typing:
		sudo apt-get install git
	2.
		$ git config --global user.name "Your Name"
		$ git config --global user.email "email@example.com"

	3.creat repository
		$ mkdir learngit
		$ cd learngit
		$ pwd
		/Users/michael/learngit
	4.init 
		$ git init
		Initialized empty Git repository in /Users/michael/learngit/.git/

	5.add readme.txt
		........ git add readme.txt
	6.commit 
		$ git commit -m "wrote a readme file"  ## -m  : message
		[master (root-commit) cb926e7] wrote a readme file
	 	1 file changed, 2 insertions(+)
	 	create mode 100644 readme.txt
	7.git add --all
*********************************************** **commit to remote repository** *****  
[source](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)  


	1.creat ssh key
		$ ssh-keygen -t rsa -C "youremail@example.com"	
		Generating public/private rsa key pair.
		Enter file in which to save the key (/home/jzhang/.ssh/id_rsa): 
		Enter passphrase (empty for no passphrase): 
		Enter same passphrase again: 
		Your identification has been saved in /home/jzhang/.ssh/id_rsa.
		Your public key has been saved in /home/jzhang/.ssh/id_rsa.pub.
		The key fingerprint is:
			SHA256:s1JHGMX2rnsWn8r06Snqxwv9lvvM06aX4fc6mN3V2Oo vcbe123@gmail.com
			The key's randomart image is:
			+---[RSA 2048]----+
			|        .o.      |
			|         oo      |
			|        ....     |
			|         .  .    |
			|        S ..   o.|
			|       . + .o ..+|
			|      . . .oo*.==|
			|       .  .+OoOO*|
			|         .+*+BEOO|
			+----[SHA256]-----+

	2. visit  [github](https://github.com/) and sign in your acount.
	3. add SSH keys   id_rsa.pub
	4. add remot repository  
		sign in GitHub & creat a new repo   ur5  &  public & Apache License
	5. commit to remote repo
 		$ git remote add origin git@github.com:VCBE123/ur5.git  ##username VCBE123 /repo name ur5
	6. push 
		$ git push -u origin master  ####push master to origin 
		error: 无法推送一些引用到 'git@github.com:VCBE123/ur5.git'
		$ git push  origin +master
	7.success!!!!
----------------------------------------
############## **[开通博客](http://blog.csdn.net/u014515463)** ###########  
~~https://github.com/VCBE123/ur5~~

*************************** *ubuntu screen cut* *************************  

	press :Prscrn    
	$ shotwell  

# 2017-9-3
---------------------------------------------
	modify the launch file:
	default robot_ip=192.168.1.5
	limit=true

	ur5_bringup.launch 	>include < kinect2_bridge.launch  delete "output =screen" >    
				>node <kinect2_viewer>
				>the hardware_interface--  just for sim speed from 1 to 0.3   

---------------------------------------------
	* download   ##[ros_controller](https://github.com/ros-controls/ros_control)
	* catkin_make successfull 
	* rosrun rqt_controller_manager rqt_controller_manager      
	  #successfull#    
		<$ rm ~/.config/ros.org/rqt_gui.ini >

	* modify the  /home/jzhang/catkin_ws/src/ur_modern_driver-master/ur5_moveit_config/config/ controller.yaml  


# 2017-9-4
-------------------------------------------
	* creat package #robot_setup_tf# to pubulish the transform matrix from camera to robot 
base_link  to kinect2_link         
	* cmake&test successfull!!!
        * add #tf_node# to #ur5_bringup.launch#   **successfull !!!** need to be fixed.

# 2017-9-6
-------------------------------------------
push the git repository   ur_modern_driver-master to remote.

# 2017-9-7
-------------------------------------------
|command|means|
|:------|:----|
|roslaunch ur_gazebo ur5.launch|仿真真实机器人|
|roslaunch ur_modern_driver ur5_bringup.launch|真实机器人连接&启动kinect2&发布tf_transformation.|
|roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=false|Rviz运动规划及仿真 1.false:真实机器人规划 2.true:gazebo仿真|

**steps**  

	1.roslaunch ur_modern_driver ur5_bringup.launch
	2.roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=false
	3.roslaunch ur5_moveit_config moveit_rviz.launch config:=true

 

**gazebo sim**  

	roslaunch ur_gazebo ur5.launch limited:=true
	roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true limited:=true
	roslaunch ur5_moveit_config moveit_rviz.launch config:=true
---------------------------------------------
**real robot**  

	1.roslaunch ur_modern_driver ur5_bringup.launch
	2.roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=false limited:=true
	3.roslaunch ur5_moveit_config moveit_rviz.launch config:=true 
~~存在一个错误~~  

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
		[ WARN] [1504789726.197600522]: Joint 'wrist_2_joint' from the starting state is outside bounds by a significant margin: [ -16.8619 ] should be in the range [ -3.14159 ], 			[ 3.14159 ] but the error above the ~start_state_max_bounds_error parameter (currently set to 0.1)
		[ WARN] [1504789726.197624957]: Joint 'wrist_3_joint' from the starting state is outside bounds by a significant margin: [ -12.4767 ] should be in the range [ -3.14159 ], [ 3.14159 ] but the error above the ~start_state_max_bounds_error parameter (currently set to 0.1)

	moveit_rviz:
		[ INFO] [1504789720.683891217]: ABORTED: Solution found but controller failed during execution
		[ INFO] [1504789726.220528773]: ABORTED: No motion plan found. No execution attempted.
		[ERROR] [1504789730.703329743]: Ignoring transform for child_frame_id "tool0_controller" from authority "unknown_publisher" because of a nan value in the transform (0.000000 0.000000 0.000000) (-nan -nan -nan -nan)
		[ERROR] [1504789730.703470849]: Ignoring transform for child_frame_id "tool0_controller" from authority "unknown_publisher" because of an invalid quaternion in the transform (-nan -nan -nan -nan)
		[ERROR] [1504789733.206470083]: Ignoring transform for child_frame_id "tool0_controller" from authority "unknown_publisher" because of a nan value in the transform (-26815634996663506497926541532838688468333027731583940734935550743870004400856709289875207645414123802522204229032200024507277818670185204752351323049951232.000000 -0.000000 -26815635023192343461629092732595116300213112174903854817200734010508414678348141019230411761179382863589389466948106287263311598361505904384281637556322304.000000) (-nan -nan -nan -nan)

--------------------------------------------------------

  **gazebo**  
  ------------------------------------------------------
 |num|comman|means|
 |:----|:----:|:----:|
 |1|roslaunch ur_gazebo ur5.launch limited:=true|载入带限制的gazebo模型 
 |2|roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true limited:=true |设置带限制路径规划仿真 
 |3|roslaunch ur5_moveit_config moveit_rviz.launch config:=true |载入带参数的rviz路径规划

# 2017-9-8
--------------------------------------------------------
Permission denied (publickey).  
fatal: Could not read from remote repository.  
[source](ttps://help.github.com/articles/changing-a-remote-s-url/ "github help")
clone from [git](git@github.com:robotic-ultrasound-image-system/ur5.git)
catkin_make *fail*

 **solve**  
install ros-kinetic-moveit-full
		
		sudo apt-get install ros-kinetic-universal-robot  solving all comple error.
------------------------------------------------------
so full step:

	1: install ubuntu 16.04			 
	2: install ROS_Kinetic_desktop_full	 	
	3: catkin_workspace init		 
	4: git clone ur5.git			  
	5: install ros-kinetic-universal-robot	 

<urgazebo.launch>


# 2017-9-9
------------------------------------------------------
**kinetic &&  kinect2**  [source](http://blog.csdn.net/lvxobrkszd/article/details/75142503)

	git clone git@github.com:OpenKinect/libfreenect2.git

[can't push origin to master?](https://github.com/KylinGu/Test/blob/master/GitLearningExp.md)  
[force to do](https://ask.helplib.com/268638)  

	git push -f origin master
[solve fatal error](https://github.com/code-iai/iai_kinect2/issues/377)  
	
	add_definitions( -fexceptions )

# 2017-9-10
------------------------------------------------------
* push ros_control-kinetic-devel to remote
* comple successs.
* add ur5.launch realrobot sim with moveit_rviz

# 2017-9-11
-----------------------------------------------------
* learn rosbag play   
* add test.launch to adapt the robot states.
* delete two files in the ur_modern_driver-master  <ur5_moveit_config> <ur_description>
  
# 2017-9-12
----------------------------------------------------
* rewrite the history.MD

# 2017-9-18
----------------------------------------------------
add moveit_commander and work fine.  
usage:  
  1. roslaunch ur_modern_driver ur5.launch  
     * launch ur_bringup / move_group  /  rviz /moveit   
  2. rosrun moveit_commander moveit_commander_cmdline.py  
  
  3. use manipulator  

  4. just enjoy it!  

tips:  
	help                show this screen
	  allow looking <true|false>       enable/disable looking around  
	  allow replanning <true|false>    enable/disable replanning  
	  constrain           clear path constraints  
	  constrain <name>    use the constraint <name> as a path constraint  
	  current             show the current state of the active group  
	  database            display the current database connection (if any)  
	  delete <name>       forget the joint values under the name <name>  
	  eef                 print the name of the end effector attached to the current group  
	  execute             execute a previously computed motion plan  
	  go <name>           plan and execute a motion to the state <name>  
	  go rand             plan and execute a motion to a random state  
	  go <dir> <dx>|      plan and execute a motion in direction up|down|left|right|forward|backward for distance <dx>  
	  ground              add a ground plane to the planning scene  
	  id|which            display the name of the group that is operated on  
	  joints              display names of the joints in the active group  
	  load [<file>]       load a set of interpreted commands from a file  
	  pick <name>         pick up object <name>  
	  place <name>        place object <name>  
	  plan <name>         plan a motion to the state <name>  
	  plan rand           plan a motion to a random state  
	  planner <name>      use planner <name> to plan next motion  
	  record <name>       record the current joint values under the name <name>  
	  rotate <x> <y> <z>  plan and execute a motion to a specified orientation (about the X,Y,Z axes)  
	  save [<file>]       save the currently known variables as a set of commands  
	  show                display the names and values of the known states  
	  show <name>         display the value of a state  
	  stop                stop the active group  
	  time                show the configured allowed planning time  
	  time <val>          set the allowed planning time  
	  tolerance           show the tolerance for reaching the goal region  
	  tolerance <val>     set the tolerance for reaching the goal region  
	  trace <on|off>      enable/disable replanning or looking around  
	  use <name>          switch to using the group named <name> (and load it if necessary)  
	  use|groups          show the group names that are already loaded  
	  vars                display the names of the known states  
	  wait <dt>           sleep for <dt> seconds  
	  x = y               assign the value of y to x  
	  x = [v1 v2...]      assign a vector of values to x  
	  x[idx] = val        assign a value to dimension idx of x  

------------------------------------------------------------
 **edit the testtcp.py**  
 using moveit api to control the robot.  
 based on forward kinematics  
 the code is simple  
 
    
    try:
	moveit_commander.roscpp_initialize(sys.argv)
	arm=moveit_commander.MoveGroupCommander('manipulator')
	end_effector_link=arm.get_end_effector_link()
	rospy.loginfo("the end effector link is:"+str(end_effector_link))
	arm.set_named_target("home")
	traj=arm.plan()
	arm.execute(traj)
	rospy.sleep(1)

	joint_position=[0,0,0,0.0820,0,-0.003]
	arm.set_joint_value_target(joint_position)
	arm.go()

	rospy.sleep(1)

	arm.remember_joint_values('saved',joint_position)
	arm.set_named_target("up")
	arm.go()
	rospy.sleep(1)
	arm.set_named_target('saved')
	arm.go()
	rospy.sleep(1)
	arm.set_named_target("up")
	arm.go()
	moveit_commander.roscpp_shutdown()
-----------------------------------------------------------

# 2017-9-19
-----------------------------------------------------------

 **#Important changes**  
 
 * Reconstruct the <ur5_moveit_config> package 
 * in which i add the new state named " **reset** " 
 * the joint state [-275° -76° 85° -102° -85° -93°]
 
 * besides that ,i reset the kinematic matrix . the sample rate is higher

------------------------------------------------------------

 I will test this changes now .if it works better, i will commit it to the remote repository.  

error:
	when processing file: /home/jzhang/catkin_ws/src/ur5-master/universal_robot-kinetic-devel/ur_description/urdf/ur5.urdf.xacro  
	included from: /home/jzhang/catkin_ws/src/ur5-master/universal_robot-kinetic-devel/ur_description/urdf/ur5_joint_limited_robot.urdf.xacro  
	unused args [limited] for include of [/home/jzhang/catkin_ws/src/ur5-master/universal_robot-kinetic-devel/ur_description/launch/ur5_upload.launch]  
	The traceback for the exception was written to the log file

solve: 
	
	edit /ur5_moveit_planning_execution.launch"  set limited =true
        edit /launch/moveit_rviz.launch">         set limited =true   
  



















