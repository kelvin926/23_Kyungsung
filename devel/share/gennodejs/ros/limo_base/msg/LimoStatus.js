// Auto-generated. Do not edit!

// (in-package limo_base.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class LimoStatus {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.vehicle_state = null;
      this.control_mode = null;
      this.battery_voltage = null;
      this.error_code = null;
      this.motion_mode = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('vehicle_state')) {
        this.vehicle_state = initObj.vehicle_state
      }
      else {
        this.vehicle_state = 0;
      }
      if (initObj.hasOwnProperty('control_mode')) {
        this.control_mode = initObj.control_mode
      }
      else {
        this.control_mode = 0;
      }
      if (initObj.hasOwnProperty('battery_voltage')) {
        this.battery_voltage = initObj.battery_voltage
      }
      else {
        this.battery_voltage = 0.0;
      }
      if (initObj.hasOwnProperty('error_code')) {
        this.error_code = initObj.error_code
      }
      else {
        this.error_code = 0;
      }
      if (initObj.hasOwnProperty('motion_mode')) {
        this.motion_mode = initObj.motion_mode
      }
      else {
        this.motion_mode = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type LimoStatus
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [vehicle_state]
    bufferOffset = _serializer.uint8(obj.vehicle_state, buffer, bufferOffset);
    // Serialize message field [control_mode]
    bufferOffset = _serializer.uint8(obj.control_mode, buffer, bufferOffset);
    // Serialize message field [battery_voltage]
    bufferOffset = _serializer.float64(obj.battery_voltage, buffer, bufferOffset);
    // Serialize message field [error_code]
    bufferOffset = _serializer.uint16(obj.error_code, buffer, bufferOffset);
    // Serialize message field [motion_mode]
    bufferOffset = _serializer.uint8(obj.motion_mode, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type LimoStatus
    let len;
    let data = new LimoStatus(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [vehicle_state]
    data.vehicle_state = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [control_mode]
    data.control_mode = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [battery_voltage]
    data.battery_voltage = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [error_code]
    data.error_code = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [motion_mode]
    data.motion_mode = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 13;
  }

  static datatype() {
    // Returns string type for a message object
    return 'limo_base/LimoStatus';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '89a12362fe9a1bc68d82a887b7cca0f7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new LimoStatus(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.vehicle_state !== undefined) {
      resolved.vehicle_state = msg.vehicle_state;
    }
    else {
      resolved.vehicle_state = 0
    }

    if (msg.control_mode !== undefined) {
      resolved.control_mode = msg.control_mode;
    }
    else {
      resolved.control_mode = 0
    }

    if (msg.battery_voltage !== undefined) {
      resolved.battery_voltage = msg.battery_voltage;
    }
    else {
      resolved.battery_voltage = 0.0
    }

    if (msg.error_code !== undefined) {
      resolved.error_code = msg.error_code;
    }
    else {
      resolved.error_code = 0
    }

    if (msg.motion_mode !== undefined) {
      resolved.motion_mode = msg.motion_mode;
    }
    else {
      resolved.motion_mode = 0
    }

    return resolved;
    }
};

module.exports = LimoStatus;
