# Robot Arm in ROS 
#####
### 1- ROS installation: 

- ##### ROS Noetic Desktop-Full Install:
````
$ sudo apt install ros-noetic-desktop-full
````
- ##### Environment setup
````
$ echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
````
- ##### initialize rosdep
````
$ sudo apt install python3-rosdep
$ sudo rosdep init
$ rosdep update
````
### 2- Robot arm pkg: 
inside catkin_ws/src
````
$ git clone https://github.com/smart-methods/arduino_robot_arm.git
$ cd .. 
$ catkin_make
````
#
#### Controlling the robot arm by joint_state_publisher
````$ roslaunch robot_arm_pkg check_motors.launch````
- ######  inside check_motors.launch i've changed the state publisher node from "state_publisher" to "robot_state_publisher" because the ROS Noetic problem 

#### Gazebo Simulation
````$ roslaunch moveit_pkg demo_gazebo.launch````

