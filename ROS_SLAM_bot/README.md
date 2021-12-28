# ROS SLAM bot with Arduino, Rasbperry Pi
#### This project is for building a robot and programming it to autonomously navigate a pre-built map. I'll walkthrough what I did in order to build this project for an autonomous ROS stack on a Raspberry Pi for Teleoperation, mapping, localization and navigation.

<img 
src="https://user-images.githubusercontent.com/49666154/145496403-223023c8-823d-47cd-9dff-706a4a9c5c3b.jpg" width="700px"  > 
#
### First of all What is SLAM?

- #### One of the popular applications of ROS is SLAM(Simultaneous Localization and Mapping). The objective of the SLAM in mobile robotics is constructing and updating the map of an unexplored environment with help of the available sensors attached to the robot which is will be used for exploring.

### Lidar sensor and SLAM
<img src="https://user-images.githubusercontent.com/49666154/145659318-f82e87b2-7955-4e3e-bb09-61fa0aca6bfd.jpg" width="340px" > <img src="https://user-images.githubusercontent.com/49666154/145659281-7670655e-9465-4756-b84b-16ba846a1927.jpg" width="310px" > 

 #### lidar is a 360-degree two-dimensional laser range scanner (LIDAR). its commonly used to make high-resolution maps, with applications in surveying and many others. Its provided by different manufactures, Each one has its own configurations with ROS. In my case I used YDLidar X2L.
 

## Building the robot
### Required components:
###### 1-Rasbperry pi 4
###### 2-Arduino UNO
###### 3-YDLidar sensor (X2L)
###### 3-L298N H-bridge
###### 4-Four DC motors 3-6 volts with wheels
###### 5-10k mAh Power supply 
###### 6-9V battery

## Setting up Raspberry Pi for ROS remote connection
##### Firstly the Raspberry Pi needs a system that has ROS in order to work with YDLidar, To shortcut this step i've dowloaded the Ubuntu 16.04 Xenial with pre-installed ROS from Ubiquity Robotics. The instructions are explained on the website. Visit https://downloads.ubiquityrobotics.com/pi.html
##### On laptop machine I installed ubuntu 20.04 with ROS Noetic. Because this will be my main machine for ROS operations.
##### On Both machines, I've set the ROS_IP and ROSMASTER_URI in the 'bashrc', Its important in order to access ROS communication masseges.
- ##### On The Raspberry Pi machine ROS_IP and ROS_MASTER_URI are same as the machine's network ip
- ##### On my laptop ROS_IP is the machine IP and ROS_MASTER_URI is the Rasbperry pi's IP. Because The ROS master node is should run on the Raspberry pi machine. 
##### example:
##### 
```` 
Rasbperry pi bashrc: export ROS_IP=192.168.200.228 export ROS_MASTER_URI=http://192.168.200.228:11311
Laptop bashrc: export ROS_IP=192.168.200.123 export ROS_MASTER_URI=http://192.168.200.228:11311
````
- ##### Connecting the Raspberry Pi to the wifi network (The laptop machine needs to connect to the same network )
```` 
$ pifi add YOURNETWOKNAME YOURNETWORKPASSWORD 
````
- ##### Connecting to the Raspberry Pi from my laptop machine over ssh (the ip would be different): 
````
$ ssh ubuntu@192.168.100.202
````

## Testing Lidar with Raspberry Pi:
again iam using the YDLIDAR X2L for this build. The first step is to install the necessary drivers which simply is a ROS package.
````
$ cd catkin_ws/src 
$ git clone https://github.com/YDLIDAR/ydlidar_ros
$ cd ..
$ catkin_make
$ roscd ydlidar_ros/startup
$ sudo chmod 777 ./*
$ sudo sh initenv.sh
$ source catkin_ws/devel/setup.bash.
$ catkin_make 
````
##### Then to run the lidar node on the Raspberry Pi  ``roslaunch ydlidar_ros lidar.launch``.
##### and to Visualize the scans in the other machine ``rosrun rviz rviz``, and by adding the topic /scan the scans should be there as shown:
![Screenshot from 2021-12-11 16-42-38](https://user-images.githubusercontent.com/49666154/145696448-d6bf2a4e-48dc-41fe-aeda-17d86d1aa535.png)



## Connection :
#### L298N H-bridge motors driver  
<img src="https://user-images.githubusercontent.com/49666154/128776326-36a2416f-9356-49f9-842e-ab9bff2704f0.jpeg" width="250px" > <img src="https://user-images.githubusercontent.com/49666154/128803887-7bc041e8-9c74-42aa-8f75-aa2c68efa30d.png" width="350px" >
###### L298N is a dual H-Bridge motor driver which allows speed and direction control of two or four DC motors at the same time.

#### from arduino to L298N Driver
- ##### ~11 connected to ENA
- #####  12 connected to INA1
- #####  13 connected to INA2
- #####   8 connected to INB4
- #####   7 connected to INB3
- #####  ~9 connected to ENB
- ##### GND connected to GND

#### Motors and Power supllies:
 ##### Two DC motors are conected to each side of L298N in parallel:
- ##### Dc motors right side: Positive to out4,Negative to out3
- ##### Dc motors left side: Positive to out1,Negative to out2
- #####  9V Battery connected to L298N GND and VCC
- #####  10k mAh power supply connected to Raspberry pi4
- ##### Arduino and YDLidar are powerd by the raspberry pi usb ports.

## Circuit Diagram:
##### Arduino and L298N
![Screenshot (254)](https://user-images.githubusercontent.com/49666154/145664909-43aead89-b663-4c01-b140-507947246565.png)
##### The Arduino and YDLidar are connected to the raspberry pi usb ports as shown
<img src="https://user-images.githubusercontent.com/49666154/145665077-49dca7bd-78b3-4274-acd1-1f0f2671fb93.jpg" width="500px" >

## Setting Arduino With ROS
##### The goal here is getting commands from the Raspberry Pi to the Arduino to move the motor. 
##### Firstly I needed to Install rosserial, a ROS module that enables Arduino-ROS communication, on both the Raspberry Pi and the Arduino to achieve that.
- ##### On Arduino IDE, I installed the rosserial library. I found it the easiest to do it from the IDE itself by searching for 'rosserial' in the Library Manager and install it. 
- ##### On the Rasbperry pi: 
````
$ sudo apt-get install ros-kinetic-rosserial-arduino
$ sudo apt-get install ros-kinetic-rosserial
$ cd catkin_ws/src
$ git clone https://github.com/ros-drivers/rosserial.git
$ cd catkin_ws
$ catkin_make
$ catkin_make install
````
###### For more information. Visit http://wiki.ros.org/rosserial_arduino/Tutorials
###### Note: i needed to override the cmake with a newer version in order to compile rosserial package. Because Ubiquity system has an old version. 
- ##### For Controling Arduino motors by ROS I've created an arduino sketch that subscribes to /cmd_vel topic and supports moving on each side and stopping motion.
> ###### Checkout:  arduino_car_ros.ino Sketch file.
- ##### In order for the arduino to operate you'll need a rosserial and teleop nodes running which are explained in the Operation section.


## Installing Hector-SLAM
##### This part is exciting! We will now add the mapping to our robot. I used the Hector-SLAM package. It enables the robot to create the maps (with a Lidar alone, no IMU needed) that I could later use for localization and navigation.

```` 
$ cd catkin_ws/src
$ git clone https://github.com/tu-darmstadt-ros-pkg/hector_slam.git
$ cd ..
$ catkin_make
$ source /catkin_ws/devel/setup.bash.
````
###### Note: before this step I've increased the Raspberry Pi swap space to 1G

##### By Reaching this point I made a couple of modifications to the Hector SLAM tutorial files in order for them to work with my build. I firstly toke a note of the transformations available to me on the \tf topic comming from the lidar node, and the reference frames it uses.
![Screenshot from 2021-12-11 17-59-19](https://user-images.githubusercontent.com/49666154/145697600-e4bb856b-373e-47b8-a0ff-586c53f8ffa8.png)

##### As you can see It has only two frames, /base_footprint and laser_frame. So I modified the necessary files as shown:
- - ###### File catkin_ws/src/hector_slam/hector_mapping/launch/mapping_default.launch:
- ##### At the top of the file, I changed the first line to the second.
````
<arg name="odom_frame" default="nav"/>
<arg name="odom_frame" default="base_footprint"/>
````
- ##### At almost the bottom of the file:
````
<node pkg="tf" type="static_transform_publisher" name="map_nav_broadcaster" args="0 0 0 0 0 0 map nav 100"/>
<node pkg="tf" type="static_transform_publisher" name="map_nav_broadcaster" args="0 0 0 0 0 0 base_footprint laser_frame 100"/>
````
- - ###### File ~/catkin_ws/src/hector_slam/hector_slam_launch/launch/tutorial.launch
##### I've changed from/to: 
````<param name="/use_sim_time" value="true"/>
<param name="/use_sim_time" value="false"/>
````
#


### Ros Operations after building the robot: 
- ###### On Raspberry Pi terminals:
````
# First terminal
$ roslauch ydlidar_ros lidar.launch
# Second terminal
$ hector_slam_launch tutorial.launch
````
- ##### For the rosserial port node and the teleop keyboard node I've created simple package that containes a launch file for both nodes.
> checkout: Navigator_bot folder.
###### Runing the launch file on Raspberry Pi:
````
$ roslaunch Navigator_bot bot_teleop.launch
````

<img src="https://user-images.githubusercontent.com/49666154/145700727-f0217789-04ec-4b18-8441-d066295f1a8c.png" width="510px" > 

- ###### On laptop machine terminal:
````
rosrun rviz rviz 
````
- ##### Then to create a map  the robot needs to move around the surface to scan in Rviz.
- ##### After the map is completed to save it I installed map server on my laptop machine:
````
$ sudo apt-get install ros-kinetic-map-server
$ rosrun map_server map_saver -f my_map
````
##### Result 
![Screenshot from 2021-12-11 18-29-56](https://user-images.githubusercontent.com/49666154/145698152-4ca6cffa-e1ef-40bf-a928-7bfd9bb85dd3.png)

### Localization 
##### In order for the navigation stack to be able to localize the robot, it needs access to the map I have just saved. Luckily its an easy task to do! The straight way to do this is by running:
``
rosrun map-server map-server my_map.yaml
``
##### And then the map is visualized with rviz and the robot is localized in it.
#
Thats is I hope you enjoyed, And please refer any issue that encounter you while following the project.

