#pragma once

#include <pluginlib/class_list_macros.h>
#include <array>
#include <string>
#include <vector>

#include <hardware_interface/joint_state_interface.h>
#include <hardware_interface/robot_hw.h>
#include <realtime_tools/realtime_publisher.h>
#include <sensor_msgs/JointState.h>

#include <franka/robot.h>

#include <franka_hw/FrankaState.h>
#include <franka_hw/franka_cartesian_state_interface.h>
#include <franka_hw/franka_joint_state_interface.h>

namespace franka_hw {

class FrankaHW : public hardware_interface::RobotHW {
 public:
  FrankaHW();

  /**
  * @param joint_names A vector of joint names for all franka joint
  * @param ip The ip address of the franka robot to connect to
  * @param nh A nodehandle e.g to register publishers
  */
  FrankaHW(const std::vector<std::string>& joint_names,
           const std::string& ip,
           const ros::NodeHandle& nh);
  ~FrankaHW() override = default;
  bool update();
  void publishFrankaStates();
  void publishJointStates();

 private:
  hardware_interface::JointStateInterface joint_state_interface_;
  franka_hw::FrankaJointStateInterface franka_joint_state_interface_;
  franka_hw::FrankaCartesianStateInterface franka_cartesian_state_interface_;
  franka::Robot robot_;
  realtime_tools::RealtimePublisher<franka_hw::FrankaState>
      publisher_franka_states_;
  realtime_tools::RealtimePublisher<sensor_msgs::JointState>
      publisher_joint_states_;
  uint64_t sequence_number_joint_states_ = 0;
  uint64_t sequence_number_franka_states_ = 0;
  uint64_t missed_publishes_franka_states_ = 0;
  uint64_t missed_publishes_joint_states_ = 0;
  std::vector<std::string> joint_name_;
  franka::RobotState robot_state_;
};

}  // namespace franka_hw