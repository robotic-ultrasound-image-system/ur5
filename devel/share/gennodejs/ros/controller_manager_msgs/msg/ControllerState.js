// Auto-generated. Do not edit!

// (in-package controller_manager_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let HardwareInterfaceResources = require('./HardwareInterfaceResources.js');

//-----------------------------------------------------------

class ControllerState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.name = null;
      this.state = null;
      this.type = null;
      this.claimed_resources = null;
    }
    else {
      if (initObj.hasOwnProperty('name')) {
        this.name = initObj.name
      }
      else {
        this.name = '';
      }
      if (initObj.hasOwnProperty('state')) {
        this.state = initObj.state
      }
      else {
        this.state = '';
      }
      if (initObj.hasOwnProperty('type')) {
        this.type = initObj.type
      }
      else {
        this.type = '';
      }
      if (initObj.hasOwnProperty('claimed_resources')) {
        this.claimed_resources = initObj.claimed_resources
      }
      else {
        this.claimed_resources = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ControllerState
    // Serialize message field [name]
    bufferOffset = _serializer.string(obj.name, buffer, bufferOffset);
    // Serialize message field [state]
    bufferOffset = _serializer.string(obj.state, buffer, bufferOffset);
    // Serialize message field [type]
    bufferOffset = _serializer.string(obj.type, buffer, bufferOffset);
    // Serialize message field [claimed_resources]
    // Serialize the length for message field [claimed_resources]
    bufferOffset = _serializer.uint32(obj.claimed_resources.length, buffer, bufferOffset);
    obj.claimed_resources.forEach((val) => {
      bufferOffset = HardwareInterfaceResources.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ControllerState
    let len;
    let data = new ControllerState(null);
    // Deserialize message field [name]
    data.name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [state]
    data.state = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [type]
    data.type = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [claimed_resources]
    // Deserialize array length for message field [claimed_resources]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.claimed_resources = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.claimed_resources[i] = HardwareInterfaceResources.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.name.length;
    length += object.state.length;
    length += object.type.length;
    object.claimed_resources.forEach((val) => {
      length += HardwareInterfaceResources.getMessageSize(val);
    });
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'controller_manager_msgs/ControllerState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'aeb6b261d97793ab74099a3740245272';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string name
    string state
    string type
    controller_manager_msgs/HardwareInterfaceResources[] claimed_resources
    
    ================================================================================
    MSG: controller_manager_msgs/HardwareInterfaceResources
    # Type of hardware interface
    string hardware_interface
    # List of resources belonging to the hardware interface
    string[] resources
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ControllerState(null);
    if (msg.name !== undefined) {
      resolved.name = msg.name;
    }
    else {
      resolved.name = ''
    }

    if (msg.state !== undefined) {
      resolved.state = msg.state;
    }
    else {
      resolved.state = ''
    }

    if (msg.type !== undefined) {
      resolved.type = msg.type;
    }
    else {
      resolved.type = ''
    }

    if (msg.claimed_resources !== undefined) {
      resolved.claimed_resources = new Array(msg.claimed_resources.length);
      for (let i = 0; i < resolved.claimed_resources.length; ++i) {
        resolved.claimed_resources[i] = HardwareInterfaceResources.Resolve(msg.claimed_resources[i]);
      }
    }
    else {
      resolved.claimed_resources = []
    }

    return resolved;
    }
};

module.exports = ControllerState;
