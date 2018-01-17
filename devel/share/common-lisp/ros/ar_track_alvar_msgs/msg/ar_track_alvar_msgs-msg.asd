
(cl:in-package :asdf)

(defsystem "ar_track_alvar_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "AlvarMarker" :depends-on ("_package_AlvarMarker"))
    (:file "_package_AlvarMarker" :depends-on ("_package"))
    (:file "AlvarMarkers" :depends-on ("_package_AlvarMarkers"))
    (:file "_package_AlvarMarkers" :depends-on ("_package"))
  ))