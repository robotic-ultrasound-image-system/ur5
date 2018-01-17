; Auto-generated. Do not edit!


(cl:in-package ar_track_alvar_msgs-msg)


;//! \htmlinclude AlvarMarkers.msg.html

(cl:defclass <AlvarMarkers> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (markers
    :reader markers
    :initarg :markers
    :type (cl:vector ar_track_alvar_msgs-msg:AlvarMarker)
   :initform (cl:make-array 0 :element-type 'ar_track_alvar_msgs-msg:AlvarMarker :initial-element (cl:make-instance 'ar_track_alvar_msgs-msg:AlvarMarker))))
)

(cl:defclass AlvarMarkers (<AlvarMarkers>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AlvarMarkers>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AlvarMarkers)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ar_track_alvar_msgs-msg:<AlvarMarkers> is deprecated: use ar_track_alvar_msgs-msg:AlvarMarkers instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <AlvarMarkers>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ar_track_alvar_msgs-msg:header-val is deprecated.  Use ar_track_alvar_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'markers-val :lambda-list '(m))
(cl:defmethod markers-val ((m <AlvarMarkers>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ar_track_alvar_msgs-msg:markers-val is deprecated.  Use ar_track_alvar_msgs-msg:markers instead.")
  (markers m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AlvarMarkers>) ostream)
  "Serializes a message object of type '<AlvarMarkers>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'markers))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'markers))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AlvarMarkers>) istream)
  "Deserializes a message object of type '<AlvarMarkers>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'markers) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'markers)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'ar_track_alvar_msgs-msg:AlvarMarker))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AlvarMarkers>)))
  "Returns string type for a message object of type '<AlvarMarkers>"
  "ar_track_alvar_msgs/AlvarMarkers")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AlvarMarkers)))
  "Returns string type for a message object of type 'AlvarMarkers"
  "ar_track_alvar_msgs/AlvarMarkers")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AlvarMarkers>)))
  "Returns md5sum for a message object of type '<AlvarMarkers>"
  "943fe17bfb0b4ea7890368d0b25ad0ad")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AlvarMarkers)))
  "Returns md5sum for a message object of type 'AlvarMarkers"
  "943fe17bfb0b4ea7890368d0b25ad0ad")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AlvarMarkers>)))
  "Returns full string definition for message of type '<AlvarMarkers>"
  (cl:format cl:nil "Header header~%AlvarMarker[] markers~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: ar_track_alvar_msgs/AlvarMarker~%Header header~%uint32 id~%uint32 confidence~%geometry_msgs/PoseStamped pose~%~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AlvarMarkers)))
  "Returns full string definition for message of type 'AlvarMarkers"
  (cl:format cl:nil "Header header~%AlvarMarker[] markers~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: ar_track_alvar_msgs/AlvarMarker~%Header header~%uint32 id~%uint32 confidence~%geometry_msgs/PoseStamped pose~%~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AlvarMarkers>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'markers) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AlvarMarkers>))
  "Converts a ROS message object to a list"
  (cl:list 'AlvarMarkers
    (cl:cons ':header (header msg))
    (cl:cons ':markers (markers msg))
))
