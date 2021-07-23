# ROS Navigation Publisher 
  ### Environment: 
  ##### UBUNTO 20.04 , Ros: Noetic
  ##### Simulation: TurtleBot3 World 
  ##### Model: burger
 #
#### STEPS:

- #### Create navigation_goal pkg with Command:
````
$ catkin_create_pkg navigation_goal rospy message_generation std_msgs geometry_msgs
````
- #### Write Python Script that publishes to  /move_base_simple/goal:
###### File:
````
 src/set_init_pose.py
````
- #### run:
````
$ rosrun navigation_goal set_init_pose.py
````
  
