# ROS Multiple Simulation with Turtlebot3
  ### Environment: 
  ##### UBUNTO 20.04 , Ros: Noetic
  ##### Simulation: TurtleBot3 World 
  ##### Model: burger
 #
#### STEPS:

- #### Create multi_sim_turtlebot3 pkg with Command:
````
$ catkin_create_pkg navigation_goal rospy 
````
- #### Write three launch files:
##### one_robot.launch:
>**Initiats the Spown model and the Robot state publisher nodes**
##### robots.launch:
>**Creates two Turtlebot3 burger robots with names and initial positions**
##### new_simulation.launch:
>**Starts turtlebot3_World World and includes all robots in robots.launch**

#
 #### run: 
- ###### Terminal 1: Gazebo simulation
````
$ roslaunch multi_sim_turtlebot3 new_simulation.launch
````
- ###### Terminal 2: robots control
````
$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py /cmd_vel:=/robot1/cmd_vel //robot1
or
rosrun teleop_twist_keyboard teleop_twist_keyboard.py /cmd_vel:=/robot1/cmd_vel  //robot2
````


  
