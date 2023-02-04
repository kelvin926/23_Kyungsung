// Generated by gencpp from file limo_base/LimoStatus.msg
// DO NOT EDIT!


#ifndef LIMO_BASE_MESSAGE_LIMOSTATUS_H
#define LIMO_BASE_MESSAGE_LIMOSTATUS_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace limo_base
{
template <class ContainerAllocator>
struct LimoStatus_
{
  typedef LimoStatus_<ContainerAllocator> Type;

  LimoStatus_()
    : header()
    , vehicle_state(0)
    , control_mode(0)
    , battery_voltage(0.0)
    , error_code(0)
    , motion_mode(0)  {
    }
  LimoStatus_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , vehicle_state(0)
    , control_mode(0)
    , battery_voltage(0.0)
    , error_code(0)
    , motion_mode(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef uint8_t _vehicle_state_type;
  _vehicle_state_type vehicle_state;

   typedef uint8_t _control_mode_type;
  _control_mode_type control_mode;

   typedef double _battery_voltage_type;
  _battery_voltage_type battery_voltage;

   typedef uint16_t _error_code_type;
  _error_code_type error_code;

   typedef uint8_t _motion_mode_type;
  _motion_mode_type motion_mode;





  typedef boost::shared_ptr< ::limo_base::LimoStatus_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::limo_base::LimoStatus_<ContainerAllocator> const> ConstPtr;

}; // struct LimoStatus_

typedef ::limo_base::LimoStatus_<std::allocator<void> > LimoStatus;

typedef boost::shared_ptr< ::limo_base::LimoStatus > LimoStatusPtr;
typedef boost::shared_ptr< ::limo_base::LimoStatus const> LimoStatusConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::limo_base::LimoStatus_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::limo_base::LimoStatus_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::limo_base::LimoStatus_<ContainerAllocator1> & lhs, const ::limo_base::LimoStatus_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.vehicle_state == rhs.vehicle_state &&
    lhs.control_mode == rhs.control_mode &&
    lhs.battery_voltage == rhs.battery_voltage &&
    lhs.error_code == rhs.error_code &&
    lhs.motion_mode == rhs.motion_mode;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::limo_base::LimoStatus_<ContainerAllocator1> & lhs, const ::limo_base::LimoStatus_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace limo_base

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::limo_base::LimoStatus_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::limo_base::LimoStatus_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::limo_base::LimoStatus_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::limo_base::LimoStatus_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::limo_base::LimoStatus_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::limo_base::LimoStatus_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::limo_base::LimoStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "89a12362fe9a1bc68d82a887b7cca0f7";
  }

  static const char* value(const ::limo_base::LimoStatus_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x89a12362fe9a1bc6ULL;
  static const uint64_t static_value2 = 0x8d82a887b7cca0f7ULL;
};

template<class ContainerAllocator>
struct DataType< ::limo_base::LimoStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "limo_base/LimoStatus";
  }

  static const char* value(const ::limo_base::LimoStatus_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::limo_base::LimoStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n"
"\n"
"uint8 vehicle_state\n"
"uint8 control_mode\n"
"float64 battery_voltage\n"
"uint16 error_code\n"
"uint8 motion_mode\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::limo_base::LimoStatus_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::limo_base::LimoStatus_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.vehicle_state);
      stream.next(m.control_mode);
      stream.next(m.battery_voltage);
      stream.next(m.error_code);
      stream.next(m.motion_mode);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct LimoStatus_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::limo_base::LimoStatus_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::limo_base::LimoStatus_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "vehicle_state: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.vehicle_state);
    s << indent << "control_mode: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.control_mode);
    s << indent << "battery_voltage: ";
    Printer<double>::stream(s, indent + "  ", v.battery_voltage);
    s << indent << "error_code: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.error_code);
    s << indent << "motion_mode: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.motion_mode);
  }
};

} // namespace message_operations
} // namespace ros

#endif // LIMO_BASE_MESSAGE_LIMOSTATUS_H
