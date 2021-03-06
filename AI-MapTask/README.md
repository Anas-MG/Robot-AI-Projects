# ROS Simultaneous Localization And Mapping (SLAM) 
![diff_drive_bot](https://user-images.githubusercontent.com/49666154/124212448-a7af6880-daf7-11eb-9d30-c1059a1e7984.png)
### Install  ROS Packages
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
## **1-Using SLAM with Waffle bot  and  turtlebot3 World Model**
### Scanned Map
![turtlebot3_AnasMP](https://user-images.githubusercontent.com/49666154/124042206-00580600-da11-11eb-9c5a-5ddc1655254b.png)


### Installation: 
- #### TurtleBot3 dependencies
````
$ sudo apt install ros-noetic-dynamixel-sdk
$ sudo apt install ros-noetic-turtlebot3-msgs
$ sudo apt install ros-noetic-turtlebot3
````
-  #### Turtlebot3 Simulation Package
 ````
$ git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
````
- #### Launch Simulation World House with waffle Bot 
 ````
$ export TURTLEBOT3_MODEL=waffle
$ roslaunch turtlebot3_gazebo turtlebot3_world.launch
 ````
 - #### Controle robot with keyboard
 ````
 $ export TURTLEBOT3_MODEL=waffle
 $ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
 ````
 - #### Run SLAM node 
 ````
$ export TURTLEBOT3_MODEL=waffle
$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
 ````
 - #### Saving the map 
````
 $ rosrun map_server map_saver -f ~/map
````

## **2-Using SLAM with diff drive bot and Turtlebot3 House Model**

### Scanned Map
![diff_drive_bot_Map](https://user-images.githubusercontent.com/49666154/124212452-a8e09580-daf7-11eb-9aff-4865f1219975.png)

## Installation :
- ##### Diff Drive robot:
````
git clone https://github.com/devanshdhrafani/diff_drive_bot.git
````
- ##### Required dependencies:
```` 
sudo apt-get install ros-noetic-dwa-local-planner
````
##
###### **The launch files in this package uses xacro.py and it is deprecated; I've used xacro instead**
##
- #### Load the robot in Gazebo environment. Default model is the turtlebot3_house
````
$ roslaunch diff_drive_bot gazebo.launch
```` 
##
 ###### **At this point i've changed node name="joint_state_publisher" in gmapping.launch to  node name="rob_st_pub" to work with my noetic** 
##

- #### Launch the SLAM gmapping node. This will also start rviz to visualize
```` 
$ roslaunch diff_drive_bot gmapping.launch
````
- #### Control using keyboard: 
````
$ rosrun diff_drive_bot keyboard_teleop.py  // This command from the source didn't work with me . i think it was duo to that it was built for older python
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch // I've used the turtlebot3_teleop_key.launch file and it worked.
````


