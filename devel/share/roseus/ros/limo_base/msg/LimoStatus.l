;; Auto-generated. Do not edit!


(when (boundp 'limo_base::LimoStatus)
  (if (not (find-package "LIMO_BASE"))
    (make-package "LIMO_BASE"))
  (shadow 'LimoStatus (find-package "LIMO_BASE")))
(unless (find-package "LIMO_BASE::LIMOSTATUS")
  (make-package "LIMO_BASE::LIMOSTATUS"))

(in-package "ROS")
;;//! \htmlinclude LimoStatus.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass limo_base::LimoStatus
  :super ros::object
  :slots (_header _vehicle_state _control_mode _battery_voltage _error_code _motion_mode ))

(defmethod limo_base::LimoStatus
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:vehicle_state __vehicle_state) 0)
    ((:control_mode __control_mode) 0)
    ((:battery_voltage __battery_voltage) 0.0)
    ((:error_code __error_code) 0)
    ((:motion_mode __motion_mode) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _vehicle_state (round __vehicle_state))
   (setq _control_mode (round __control_mode))
   (setq _battery_voltage (float __battery_voltage))
   (setq _error_code (round __error_code))
   (setq _motion_mode (round __motion_mode))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:vehicle_state
   (&optional __vehicle_state)
   (if __vehicle_state (setq _vehicle_state __vehicle_state)) _vehicle_state)
  (:control_mode
   (&optional __control_mode)
   (if __control_mode (setq _control_mode __control_mode)) _control_mode)
  (:battery_voltage
   (&optional __battery_voltage)
   (if __battery_voltage (setq _battery_voltage __battery_voltage)) _battery_voltage)
  (:error_code
   (&optional __error_code)
   (if __error_code (setq _error_code __error_code)) _error_code)
  (:motion_mode
   (&optional __motion_mode)
   (if __motion_mode (setq _motion_mode __motion_mode)) _motion_mode)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint8 _vehicle_state
    1
    ;; uint8 _control_mode
    1
    ;; float64 _battery_voltage
    8
    ;; uint16 _error_code
    2
    ;; uint8 _motion_mode
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint8 _vehicle_state
       (write-byte _vehicle_state s)
     ;; uint8 _control_mode
       (write-byte _control_mode s)
     ;; float64 _battery_voltage
       (sys::poke _battery_voltage (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; uint16 _error_code
       (write-word _error_code s)
     ;; uint8 _motion_mode
       (write-byte _motion_mode s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint8 _vehicle_state
     (setq _vehicle_state (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _control_mode
     (setq _control_mode (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float64 _battery_voltage
     (setq _battery_voltage (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; uint16 _error_code
     (setq _error_code (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint8 _motion_mode
     (setq _motion_mode (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get limo_base::LimoStatus :md5sum-) "89a12362fe9a1bc68d82a887b7cca0f7")
(setf (get limo_base::LimoStatus :datatype-) "limo_base/LimoStatus")
(setf (get limo_base::LimoStatus :definition-)
      "Header header

uint8 vehicle_state
uint8 control_mode
float64 battery_voltage
uint16 error_code
uint8 motion_mode

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
string frame_id

")



(provide :limo_base/LimoStatus "89a12362fe9a1bc68d82a887b7cca0f7")


