#include "ros/ros.h"
#include "tf/transform_listener.h"
#include "tf/message_filter.h"
#include "message_filters/subscriber.h" 
class PoseTrans
{
  public:
  PoseTrans() : tf_(),  target_frame_("base_link")
   {
     pose_sub_.subscribe(n_,"/ar_pose_marker", 1);
     tf_filter_ = new tf::MessageFilter<geometry_msgs::PoseStamped>(pose_sub_, tf_, target_frame_, 10);
      tf_filter_->registerCallback( boost::bind(&PoseTrans::msgCallback, this, _1) );
   }
  private:
    message_filters::Subscriber<geometry_msgs::PoseStamped> pose_sub_;
    tf::TransformListener tf_;
    tf::MessageFilter<geometry_msgs::PoseStamped> * tf_filter_;
    ros::NodeHandle n_;
    std::string target_frame_;
    ros::Publisher basepose=n_.advertise<geometry_msgs::PoseStamped>("/pose_trans",1);
 
     //  Callback to register with tf::MessageFilter to be called when transforms are available
    void msgCallback(const boost::shared_ptr<const geometry_msgs::PoseStamped>& pose_ptr) 
     {
       geometry_msgs::PoseStamped pose_out;
       try 
       {
         tf_.transformPose(target_frame_, *pose_ptr, pose_out);
         
         basepose.publish(pose_out);
         ros::spinOnce();
         printf("pose target in frame of base_link Position(x:%f y:%f z:%f)\n", 
                pose_out.pose.position.x,
                pose_out.pose.position.y,
                pose_out.pose.position.z);
         
       }
       catch (tf::TransformException &ex) 
       {
         printf ("Failure %s\n", ex.what()); //Print exception which was caught
       }
     };
   
   };
   
   
   int main(int argc, char ** argv)
   {
   ros::init(argc, argv, "pose_trans"); //Init ROS
   PoseTrans pd; //Construct class
   ros::spin(); // Run until interupted 
  };

