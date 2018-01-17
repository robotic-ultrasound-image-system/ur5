#!/usr/bin/env python
import argparse
import rospy
import sys
import moveit_commander
import actionlib
import roslib; roslib.load_manifest('ur_modern_driver')
from control_msgs.msg import *
from trajectory_msgs.msg import *
from sensor_msgs.msg import JointState
class JointRecorder(object):
    def __init__(self, filename, rate):
        """
        Records joint data to a file at a specified rate.
        """
        self._filename = filename
        self._raw_rate = rate
        self._rate = rospy.Rate(rate)
        self._start_time = rospy.get_time()
        self._done = False
        #self._limb_left = baxter_interface.Limb("left")
        #self._limb_right = baxter_interface.Limb("right")

    def _time_stamp(self):
        return rospy.get_time() - self._start_time
    def stop(self):
        """
        Stop recording.
        """
        self._done = True

    def done(self):
        """
        Return whether or not recording is done.
        """
        if rospy.is_shutdown():
            self.stop()
        return self._done

    def record(self):
        if self._filename:
           
            with open(self._filename, 'w') as f:
                f.write('time,')
		moveit_commander.roscpp_initialize(sys.argv)
	        arm=moveit_commander.MoveGroupCommander('manipulator')
        	end_effector_link=arm.get_end_effector_link()
                f.write('		    ,x		,y		  ,z		    ,rx		    ,ry		    ,rz		  ,rw	\n')
                #f.write(','.join([j for j in joints_right]) + '\n')	
                while not self.done():
                    #current_pose = self._limb_left.endpoint_pose()
                    current_pose=arm.get_current_pose().pose
		    timestamp=[arm.get_current_pose().header.stamp]
		    f.write("%f,".join([str(x) for x in timestamp]))
		    f.write(',')
                    endpoint_pose_position = [current_pose.position.x,
                                          current_pose.position.y,
                                          current_pose.position.z]
                    endpoint_pose_orientation = [current_pose.orientation.x,
                                           current_pose.orientation.y,
                                           current_pose.orientation.z,
                                           current_pose.orientation.w,]
                   # current_pose = self._limb_right.endpoint_pose()                      
                   #endpoint_pose_position_right = [current_pose['position'].x,
                   #                        current_pose['position'].y,
                   #                       current_pose['position'].z,]
                   # endpoint_pose_orientation_right = [current_pose['orientation'].x,
                   #                        current_pose['orientation'].y,
                   #                        current_pose['orientation'].z,
                   #                        current_pose['orientation'].w,]                     

                 
                    f.write(','.join([str(x) for x in endpoint_pose_position]) + ',')
                   # f.write(','.join([str(x) for x in endpoint_pose_position_right]) + ',')
                    f.write(','.join([str(x) for x in endpoint_pose_orientation]) + '\n')
                   # f.write(','.join([str(x) for x in endpoint_pose_orientation_right]) + '\n')
                    self._rate.sleep()
def main():
    epilog = """
    Related examples:
    joint_position_file_playback.py; joint_trajectory_file_playback.py.
    """
    arg_fmt = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=arg_fmt,
                                     description=main.__doc__,
                                     epilog=epilog)
    required = parser.add_argument_group('required arguments')
    required.add_argument(
        '-f', '--file', dest='filename', required=True,
        help='the file name to record to'
    )
    parser.add_argument(
        '-r', '--record-rate', type=int, default=20, metavar='RECORDRATE',
        help='rate at which to record (default: 100)'
    )
    args = parser.parse_args(rospy.myargv()[1:])
    print("Initializing node... ")
    
    rospy.init_node("recorder",anonymous=False) 
    print("Getting robot state... ")
    print("Enabling robot... ")
    Recorder = JointRecorder(args.filename, args.record_rate)
    rospy.on_shutdown(Recorder.stop)
    print("Recording. Press Ctrl-C to stop.")
    Recorder.record()
    print("\nDone.")
if __name__ == '__main__':
    main()
