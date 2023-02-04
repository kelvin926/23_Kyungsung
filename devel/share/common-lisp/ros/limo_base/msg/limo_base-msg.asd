
(cl:in-package :asdf)

(defsystem "limo_base-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "LimoStatus" :depends-on ("_package_LimoStatus"))
    (:file "_package_LimoStatus" :depends-on ("_package"))
  ))