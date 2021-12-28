
## Micro-ros project with ESP32 and freeRTOS
![esp32_cut](https://user-images.githubusercontent.com/49666154/130994513-0111f229-2535-478b-a06a-685c9498a55b.png)

### What is Micro Ros?
##### In shortcut Micro-Ros is Ros2 younger sibling, it puts ROS2 onto microcontrollers so we can publish and subscribe from microcontrollers to Ros2 .
##
##### Micro-ROS offers seven key features that make it ready for use in microcontroller-based robotic project:

###### ✔ Microcontroller-optimized client API supporting all major ROS concepts

###### ✔ Seamless integration with ROS 2

###### ✔ Extremely resource-constrained but flexible middleware

###### ✔ Multi-RTOS support with generic build system

###### ✔ Permissive license

###### ✔ Vibrant community and ecosystem

###### ✔ Long-term maintainability and interoperability

#
### ESP32 and FreeRTOS:
##### ESP32 makes use of FreeRTOS(Real Time Operating System) one of the three RTOSes officially supported by the micro-ROS project, which is natively used by this family of boards, and supports the latest Foxy release of ROS 2. It works both with serial and Wi-Fi transports

#
### Project Goal:
##### The main goal in this project is to learn how to publish a Ros2 topic from Esp32 board to specific IP address , I've used freeRTOS demo app called 'in32publisher' which is an available project that comes with the installation of Micro-ros.

##
### Installation:
###### before setting up Micro-ros, you'll need to install Ros2 in the local machine to recieve ics from Micro-Ros, I've Used the offical documentation guide to installation via debian pkg https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html.

#### Micro-ROS build system: 
````
# Source ROS 2 installation
echo 'source /opt/ros/foxy/setup.bash' >> ~/.bashrc

# Install colcon-core and commonly used extension packages in order to build Mirco-ros tools
sudo apt update
sudo apt install python3-colcon-common-extensions

# Create a workspace and download the micro-ROS tools
mkdir microros_ws
cd microros_ws
git clone -b foxy https://github.com/micro-ROS/micro_ros_setup.git src/micro_ros_setup

# Update dependencies using rosdep
rosdep update
rosdep install --from-path src --ignore-src -y

# Install pip
sudo apt-get install python3-pip

# Build Micro-ros tools
colcon build

# Source Micro-ros installation
echo 'source install/local_setup.bash' >> ~/.bashrc
````

#### Build and flash ESP32 with freertos demo app called 'int32_publisher'
````
cd microros_ws
ros2 run micro_ros_setup create_firmware_ws.sh freertos esp32
ros2 run micro_ros_setup configure_firmware.sh int32_publisher -t udp -i [your local machine IP] -p 8888
ros2 run micro_ros_setup build_firmware.sh menuconfig

# Now go to the micro-ROS Transport Settings → WiFi Configuration menu, fill your local WiFi SSID and password. Save your changes, exit, and run:
ros2 run micro_ros_setup build_firmware.sh

# Connect your ESP32 to the computer, and run:
ros2 run micro_ros_setup flash_firmware.sh
````

#### Setup Micro-ros Agent: 
````
cd microros_ws
# Download micro-ROS-Agent packages
ros2 run micro_ros_setup create_agent_ws.sh

# Build 
ros2 run micro_ros_setup build_agent.sh

# Run a micro-ROS agent << this step should be done before running the ESP32 board
ros2 run micro_ros_agent micro_ros_agent udp4 --port 8888
````
## Result
##### Agent
![Screenshot from 2021-08-27 00-12-50](https://user-images.githubusercontent.com/49666154/131087937-9c35439c-00a1-4e65-9a02-7700180a89e7.png)

##### topic list
![Screenshot from 2021-08-27 00-17-32](https://user-images.githubusercontent.com/49666154/131088496-16455499-6ddc-4ed7-8893-44279831ccf5.png)

##### Subscribing to /freertos_int32_publisher 
![Screenshot from 2021-08-27 00-18-45](https://user-images.githubusercontent.com/49666154/131088508-f45f6365-19f5-4099-85ea-07c432b95d05.png)



