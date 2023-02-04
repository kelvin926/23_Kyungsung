; Auto-generated. Do not edit!


(cl:in-package limo_base-msg)


;//! \htmlinclude LimoStatus.msg.html

(cl:defclass <LimoStatus> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (vehicle_state
    :reader vehicle_state
    :initarg :vehicle_state
    :type cl:fixnum
    :initform 0)
   (control_mode
    :reader control_mode
    :initarg :control_mode
    :type cl:fixnum
    :initform 0)
   (battery_voltage
    :reader battery_voltage
    :initarg :battery_voltage
    :type cl:float
    :initform 0.0)
   (error_code
    :reader error_code
    :initarg :error_code
    :type cl:fixnum
    :initform 0)
   (motion_mode
    :reader motion_mode
    :initarg :motion_mode
    :type cl:fixnum
    :initform 0))
)

(cl:defclass LimoStatus (<LimoStatus>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LimoStatus>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LimoStatus)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name limo_base-msg:<LimoStatus> is deprecated: use limo_base-msg:LimoStatus instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <LimoStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader limo_base-msg:header-val is deprecated.  Use limo_base-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'vehicle_state-val :lambda-list '(m))
(cl:defmethod vehicle_state-val ((m <LimoStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader limo_base-msg:vehicle_state-val is deprecated.  Use limo_base-msg:vehicle_state instead.")
  (vehicle_state m))

(cl:ensure-generic-function 'control_mode-val :lambda-list '(m))
(cl:defmethod control_mode-val ((m <LimoStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader limo_base-msg:control_mode-val is deprecated.  Use limo_base-msg:control_mode instead.")
  (control_mode m))

(cl:ensure-generic-function 'battery_voltage-val :lambda-list '(m))
(cl:defmethod battery_voltage-val ((m <LimoStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader limo_base-msg:battery_voltage-val is deprecated.  Use limo_base-msg:battery_voltage instead.")
  (battery_voltage m))

(cl:ensure-generic-function 'error_code-val :lambda-list '(m))
(cl:defmethod error_code-val ((m <LimoStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader limo_base-msg:error_code-val is deprecated.  Use limo_base-msg:error_code instead.")
  (error_code m))

(cl:ensure-generic-function 'motion_mode-val :lambda-list '(m))
(cl:defmethod motion_mode-val ((m <LimoStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader limo_base-msg:motion_mode-val is deprecated.  Use limo_base-msg:motion_mode instead.")
  (motion_mode m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LimoStatus>) ostream)
  "Serializes a message object of type '<LimoStatus>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'vehicle_state)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'control_mode)) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'battery_voltage))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'error_code)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'error_code)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'motion_mode)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LimoStatus>) istream)
  "Deserializes a message object of type '<LimoStatus>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'vehicle_state)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'control_mode)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'battery_voltage) (roslisp-utils:decode-double-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'error_code)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'error_code)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'motion_mode)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LimoStatus>)))
  "Returns string type for a message object of type '<LimoStatus>"
  "limo_base/LimoStatus")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LimoStatus)))
  "Returns string type for a message object of type 'LimoStatus"
  "limo_base/LimoStatus")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LimoStatus>)))
  "Returns md5sum for a message object of type '<LimoStatus>"
  "89a12362fe9a1bc68d82a887b7cca0f7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LimoStatus)))
  "Returns md5sum for a message object of type 'LimoStatus"
  "89a12362fe9a1bc68d82a887b7cca0f7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LimoStatus>)))
  "Returns full string definition for message of type '<LimoStatus>"
  (cl:format cl:nil "Header header~%~%uint8 vehicle_state~%uint8 control_mode~%float64 battery_voltage~%uint16 error_code~%uint8 motion_mode~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LimoStatus)))
  "Returns full string definition for message of type 'LimoStatus"
  (cl:format cl:nil "Header header~%~%uint8 vehicle_state~%uint8 control_mode~%float64 battery_voltage~%uint16 error_code~%uint8 motion_mode~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LimoStatus>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     1
     1
     8
     2
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LimoStatus>))
  "Converts a ROS message object to a list"
  (cl:list 'LimoStatus
    (cl:cons ':header (header msg))
    (cl:cons ':vehicle_state (vehicle_state msg))
    (cl:cons ':control_mode (control_mode msg))
    (cl:cons ':battery_voltage (battery_voltage msg))
    (cl:cons ':error_code (error_code msg))
    (cl:cons ':motion_mode (motion_mode msg))
))
