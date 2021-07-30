# ROS Navigation Publisher 
##### The project is for the robot to navigate to a specific coordinates , the approach here is publishing a navigation goal to the robot from the python script
![send_nav_topic](https://user-images.githubusercontent.com/49666154/127578364-0cb5bf83-0cdf-4052-9ec6-551991f66e1d.png)

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
###### Script file:
``src/set_init_pose.py``
#
- #### run: (after running Gazebo and Navigation )
``$ rosrun navigation_goal set_init_pose.py``
  
