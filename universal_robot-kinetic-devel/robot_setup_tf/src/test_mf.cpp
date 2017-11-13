#include "ros/ros.h"
#include "tf/transform_listener.h"
#include "tf/message_filter.h"
#include "message_filters/subscriber.h" 
class PoseDrawer
{
  public:
  PoseDrawer() : tf_(),  target_frame_("base_link")
   {
     point_sub_.subscribe(n_, "/kinect2/click_point/left", 10);
     tf_filter_ = new tf::MessageFilter<geometry_msgs::PointStamped>(point_sub_, tf_, target_frame_, 10);
      tf_filter_->registerCallback( boost::bind(&PoseDrawer::msgCallback, this, _1) );
   } ;
  private:
    message_filters::Subscriber<geometry_msgs::PointStamped> point_sub_;
    tf::TransformListener tf_;
    tf::MessageFilter<geometry_msgs::PointStamped> * tf_filter_;
    ros::NodeHandle n_;
    std::string target_frame_;
    ros::Publisher basepoint=n_.advertise<geometry_msgs::PointStamped>("/pose_drawer",1);
 
     //  Callback to register with tf::MessageFilter to be called when transforms are available
    void msgCallback(const boost::shared_ptr<const geometry_msgs::PointStamped>& point_ptr) 
     {
       geometry_msgs::PointStamped point_out;
       try 
       {
         tf_.transformPoint(target_frame_, *point_ptr, point_out);
         
         basepoint.publish(point_out);
         ros::spinOnce();
         printf("point target in frame of base_link Position(x:%f y:%f z:%f)\n", 
                point_out.point.x,
                point_out.point.y,
                point_out.point.z);
         
       }
       catch (tf::TransformException &ex) 
       {
         printf ("Failure %s\n", ex.what()); //Print exception which was caught
       }
     };
   
   };
   
   
   int main(int argc, char ** argv)
   {
   ros::init(argc, argv, "pose_drawer"); //Init ROS
   PoseDrawer pd; //Construct class
   ros::spin(); // Run until interupted 
  };
