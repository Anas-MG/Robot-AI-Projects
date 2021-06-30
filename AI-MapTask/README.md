
## turtlebot3 Commands: 
>PC setup 
````
$ sudo apt update
$ sudo apt upgrade
$ wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_noetic.sh
$ chmod 755 ./install_ros_noetic.sh 
$ bash ./install_ros_noetic.sh
````
- ##### Install  ROS Packages
````
$ sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
  ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
  ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
  ros-noetic-rosserial-python ros-noetic-rosserial-client \
  ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
  ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
  ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
  ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers
````
- ##### Install TurtleBot3 via Debian Packages.
````
$ sudo apt install ros-noetic-dynamixel-sdk
$ sudo apt install ros-noetic-turtlebot3-msgs
$ sudo apt install ros-noetic-turtlebot3
````
- ##### update the ROS IP settings
 ```` 
 $ ifconfig // to find the IP address
 $ nano ~/.bashrc // to edit ROS_MASTER_URI and ROS_HOSTNAME with the correct IP
 $ source ~/.bashrc
````
##
>simulation:
-  ##### Install Simulation Package
 ````
$ cd ~/catkin_ws/src/
$ git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
$ cd ~/catkin_ws && catkin_make
````
- ##### Launch Simulation World for Turtlebot3 House
 ````
$ export TURTLEBOT3_MODEL=waffle_pi
$ roslaunch turtlebot3_gazebo turtlebot3_house.launch
 ````
 - #### Launce The Teleopration node to teleport Turtlebot3 robot 
 ````
 $ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
 ````
 - ##### Run SLAM node
 ````
$ export TURTLEBOT3_MODEL=waffle_pi
$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping

 ````
 - ##### Svaing the map 
 ````
 $ rosrun map_server map_saver -f ~/map
 ````
