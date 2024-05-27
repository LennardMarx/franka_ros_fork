# Notes to self

NOTE: Launch master might be necessary
```
rosnode kill -a
roscore
```

## Launch panda
```
roslaunch franka_gazebo panda.launch
```

## Launch TCP endpoint
```
roslaunch ros_tcp_endpoint endpoint.launch
```

## Launch controllers 

To work with gazebo simply launch gazebo in another terminal first, then launch edited controller script excluding the include parameter for the physical robot:
```xml
<?xml version="1.0" ?>
<launch>
  <arg name="robot" default="panda" doc="choose your robot. Possible values: [panda, fr3]"/>
  <arg name="arm_id" default="$(arg robot)" />
  <!-- <include file="$(find franka_control)/launch/franka_control.launch" pass_all_args="true"/> -->
  <rosparam command="load" file="$(find franka_example_controllers)/config/franka_example_controllers.yaml" subst_value="true" />
  <node name="controller_spawner" pkg="controller_manager" type="spawner" respawn="false" output="screen"  args="joint_velocity_example_controller"/>
  <node pkg="rviz" type="rviz" output="screen" name="rviz" args="-d $(find franka_example_controllers)/launch/robot.rviz -f $(arg arm_id)_link0 --splash-screen $(find franka_visualization)/splash.png"/>
</launch>
```



# ROS integration for Franka Robotics research robots

[![CI](https://github.com/frankaemika/franka_ros/actions/workflows/ci.yml/badge.svg)](https://github.com/frankaemika/franka_ros/actions/workflows/ci.yml)


See the [Franka Control Interface (FCI) documentation][fci-docs] for more information.

## License

All packages of `franka_ros` are licensed under the [Apache 2.0 license][apache-2.0].

[apache-2.0]: https://www.apache.org/licenses/LICENSE-2.0.html
[fci-docs]: https://frankaemika.github.io/docs
