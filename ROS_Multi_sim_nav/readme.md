# ROS Multiple robots Simulation & control with Turtlebot3
![gazebo_Screenshot](https://user-images.githubusercontent.com/49666154/127594128-31af61a5-7a55-4261-aa0e-676445b7af92.png)
  ### Environment: 
  ##### UBUNTO 20.04 , Ros: Noetic
  ##### Simulation: TurtleBot3 World 
  ##### Model: burger
 #
#### STEPS:

- #### multi_sim_turtlebot3 pkg is for multiple gazebo simulation Created with Command:
````
$ catkin_create_pkg multi_sim_turtlebot3 rospy 
````
- #### Wrote three launch files:
#### one_robot.launch:
> #####  **Initiats the Spown model and the Robot state publisher nodes**
#### robots.launch:
> ##### **Creates two Turtlebot3 burger robots with names and initial positions**
#### new_simulation.launch:
> #####  **Starts turtlebot3_World World and includes all robots in robots.launch**

#
 #### run: 
- ###### Terminal 1: Gazebo simulation
````
$ roslaunch multi_sim_turtlebot3 new_simulation.launch
````
- ###### Terminal 2: robots control
````
$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py /cmd_vel:=/robot1/cmd_vel //robot1

$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py /cmd_vel:=/robot1/cmd_vel  //robot2
````


  
