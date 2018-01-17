;; Auto-generated. Do not edit!


(when (boundp 'controller_manager_msgs::ControllerState)
  (if (not (find-package "CONTROLLER_MANAGER_MSGS"))
    (make-package "CONTROLLER_MANAGER_MSGS"))
  (shadow 'ControllerState (find-package "CONTROLLER_MANAGER_MSGS")))
(unless (find-package "CONTROLLER_MANAGER_MSGS::CONTROLLERSTATE")
  (make-package "CONTROLLER_MANAGER_MSGS::CONTROLLERSTATE"))

(in-package "ROS")
;;//! \htmlinclude ControllerState.msg.html


(defclass controller_manager_msgs::ControllerState
  :super ros::object
  :slots (_name _state _type _claimed_resources ))

(defmethod controller_manager_msgs::ControllerState
  (:init
   (&key
    ((:name __name) "")
    ((:state __state) "")
    ((:type __type) "")
    ((:claimed_resources __claimed_resources) (let (r) (dotimes (i 0) (push (instance controller_manager_msgs::HardwareInterfaceResources :init) r)) r))
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _state (string __state))
   (setq _type (string __type))
   (setq _claimed_resources __claimed_resources)
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:state
   (&optional __state)
   (if __state (setq _state __state)) _state)
  (:type
   (&optional __type)
   (if __type (setq _type __type)) _type)
  (:claimed_resources
   (&rest __claimed_resources)
   (if (keywordp (car __claimed_resources))
       (send* _claimed_resources __claimed_resources)
     (progn
       (if __claimed_resources (setq _claimed_resources (car __claimed_resources)))
       _claimed_resources)))
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; string _state
    4 (length _state)
    ;; string _type
    4 (length _type)
    ;; controller_manager_msgs/HardwareInterfaceResources[] _claimed_resources
    (apply #'+ (send-all _claimed_resources :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; string _state
       (write-long (length _state) s) (princ _state s)
     ;; string _type
       (write-long (length _type) s) (princ _type s)
     ;; controller_manager_msgs/HardwareInterfaceResources[] _claimed_resources
     (write-long (length _claimed_resources) s)
     (dolist (elem _claimed_resources)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _state
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _type
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _type (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; controller_manager_msgs/HardwareInterfaceResources[] _claimed_resources
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _claimed_resources (let (r) (dotimes (i n) (push (instance controller_manager_msgs::HardwareInterfaceResources :init) r)) r))
     (dolist (elem- _claimed_resources)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get controller_manager_msgs::ControllerState :md5sum-) "aeb6b261d97793ab74099a3740245272")
(setf (get controller_manager_msgs::ControllerState :datatype-) "controller_manager_msgs/ControllerState")
(setf (get controller_manager_msgs::ControllerState :definition-)
      "string name
string state
string type
controller_manager_msgs/HardwareInterfaceResources[] claimed_resources

================================================================================
MSG: controller_manager_msgs/HardwareInterfaceResources
# Type of hardware interface
string hardware_interface
# List of resources belonging to the hardware interface
string[] resources

")



(provide :controller_manager_msgs/ControllerState "aeb6b261d97793ab74099a3740245272")


