#include <ros/ros.h>
#include <tf/transform_broadcaster.h>

int main(int argc ,char** argv)
 {
	ros::init(argc,argv,"robot_tf_publisher");
	ros::NodeHandle n;
	
	ros::Rate r(50);
	tf::TransformBroadcaster broadcaster;

	while(n.ok()){
	broadcaster.sendTransform(
	  tf::StampedTransform(
		tf::Transform(tf::Quaternion(-0.448,0.5977,0.6344,0.1982),tf::Vector3(-0.279,-0.6866,0.4460)),
		ros::Time::now(),"base_link","kinect2_link"));
		r.sleep();

	}



 }
