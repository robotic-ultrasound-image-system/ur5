;; Auto-generated. Do not edit!


(when (boundp 'ar_track_alvar_msgs::AlvarMarkers)
  (if (not (find-package "AR_TRACK_ALVAR_MSGS"))
    (make-package "AR_TRACK_ALVAR_MSGS"))
  (shadow 'AlvarMarkers (find-package "AR_TRACK_ALVAR_MSGS")))
(unless (find-package "AR_TRACK_ALVAR_MSGS::ALVARMARKERS")
  (make-package "AR_TRACK_ALVAR_MSGS::ALVARMARKERS"))

(in-package "ROS")
;;//! \htmlinclude AlvarMarkers.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass ar_track_alvar_msgs::AlvarMarkers
  :super ros::object
  :slots (_header _markers ))

(defmethod ar_track_alvar_msgs::AlvarMarkers
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:markers __markers) (let (r) (dotimes (i 0) (push (instance ar_track_alvar_msgs::AlvarMarker :init) r)) r))
    )
   (send-super :init)
   (setq _header __header)
   (setq _markers __markers)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:markers
   (&rest __markers)
   (if (keywordp (car __markers))
       (send* _markers __markers)
     (progn
       (if __markers (setq _markers (car __markers)))
       _markers)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; ar_track_alvar_msgs/AlvarMarker[] _markers
    (apply #'+ (send-all _markers :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; ar_track_alvar_msgs/AlvarMarker[] _markers
     (write-long (length _markers) s)
     (dolist (elem _markers)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; ar_track_alvar_msgs/AlvarMarker[] _markers
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _markers (let (r) (dotimes (i n) (push (instance ar_track_alvar_msgs::AlvarMarker :init) r)) r))
     (dolist (elem- _markers)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get ar_track_alvar_msgs::AlvarMarkers :md5sum-) "943fe17bfb0b4ea7890368d0b25ad0ad")
(setf (get ar_track_alvar_msgs::AlvarMarkers :datatype-) "ar_track_alvar_msgs/AlvarMarkers")
(setf (get ar_track_alvar_msgs::AlvarMarkers :definition-)
      "Header header
AlvarMarker[] markers

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: ar_track_alvar_msgs/AlvarMarker
Header header
uint32 id
uint32 confidence
geometry_msgs/PoseStamped pose


================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :ar_track_alvar_msgs/AlvarMarkers "943fe17bfb0b4ea7890368d0b25ad0ad")


