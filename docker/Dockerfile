FROM ros:kinetic-ros-base

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y git curl

# Set the default directory where CMD will execute
WORKDIR /catkin_ws

ADD . /catkin_ws

#Install multirobot map merge package
RUN apt-get install -y ros-kinetic-multirobot-map-merge

#Install gezebo
RUN apt-get install -y ros-kinetic-gazebo-ros-pkgs ros-kinetic-gazebo-ros-control

# Install turtlebot packages
RUN apt-get install -y ros-kinetic-turtlebot-description ros-kinetic-turtlebot-bringup ros-kinetic-turtlebot-navigation ros-kinetic-turtlebot-teleop

# Install rviz
RUN apt-get install -y ros-kinetic-rviz

# Configure environment
CMD ["/bin/bash", "entrypoint.sh"]


# To run that img
#xhost +local:root
#docker run -it -e DISPLAY -e QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix:rw --device /dev/dri -it --rm <name of img>
#xhost -local:root
