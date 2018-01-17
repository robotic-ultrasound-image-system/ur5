#include "ros/ros.h"
#include "tf/transform_listener.h"
#include "tf/message_filter.h"
#include "message_filters/subscriber.h" 
#include <nav_msgs/Path.h>
#include <vector>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>  
#include <vector>  
#include <list>  
#include <deque>  
#include <string>  
#include <numeric>  
#include <algorithm>


class PathTrans
{
  public:
  PathTrans() : tf_(),  target_frame_("base_link")
   {
     path_sub_.subscribe(n_,"/kinect2/path_navigation", 1);
     tf_filter_ = new tf::MessageFilter<nav_msgs::Path>(path_sub_, tf_, target_frame_, 10);
      tf_filter_->registerCallback( boost::bind(&PathTrans::msgCallback, this, _1) );
   } ;
  private:
    tf::StampedTransform transform;
    message_filters::Subscriber<nav_msgs::Path> path_sub_;
    tf::TransformListener tf_;
    tf::MessageFilter<nav_msgs::Path> * tf_filter_;
    ros::NodeHandle n_;
    std::string target_frame_;
    ros::Publisher basepath=n_.advertise<nav_msgs::Path>("/path_trans",1);
    std::vector<geometry_msgs::PoseStamped>::const_iterator itor;
    float x;
    float y;
    float z;
    float w;
     //  Callback to register with tf::MessageFilter to be called when transforms are available
    void msgCallback(const boost::shared_ptr<const nav_msgs::Path>& path_ptr) 
     {
       nav_msgs::Path path_out;
       geometry_msgs::PoseStamped pose_out;
       geometry_msgs::PoseStamped pose_ptr;
       itor=path_ptr->poses.begin();
       while(itor++!=path_ptr->poses.end())
  	 {   
    
      	 	try 
      	 	{
                x= itor->pose.orientation.x;
		y= itor->pose.orientation.y;
		z= itor->pose.orientation.z;
		w= itor->pose.orientation.w;
                 tf_.lookupTransform(target_frame_,"/kinect2_link" , ros::Time(0), transform);
        	 printf("path target in frame of kinect2_link Position(x:%f y:%f z:%f,rx:%f ry:%f rz:%f rw:%f)\n", 
        	 itor->pose.position.x,
        	 itor->pose.position.y,
        	 itor->pose.position.z,
		 x,
		 y,
		 z,
		 w);               
			if((x*x+y*y+z*z+w*w)==1&&itor->pose.position.x<10)
			{tf_.transformPose(target_frame_, *itor, pose_out);
        	 	path_out.poses.push_back(pose_out);
			x= pose_out.pose.orientation.x;
			y= pose_out.pose.orientation.y;
			z=pose_out.pose.orientation.z;
			w= pose_out.pose.orientation.w;
 			printf("path target in frame of base_link Position(x:%f y:%f z:%f,rx:%f ry:%f rz:%f rw:%f)\n", 
        	 	pose_out.pose.position.x,
        	 	pose_out.pose.position.y,
        		pose_out.pose.position.z,
		 	x,
		 	y,
		 	z,
		 	w);         }       	         	
        	
         
       		}
       		catch (tf::TransformException &ex) 
       		{
        	 printf ("Failure %s\n", ex.what()); //Print exception which was caught
       		}
         }
	 basepath.publish(path_out);
 	

       
   
     };




   
   };
   
   
   int main(int argc, char ** argv)
   {
   ros::init(argc, argv, "path_trans"); //Init ROS
   PathTrans pd; //Construct class
   ros::spin(); // Run until interupted 
  };
