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

#Install rviz
RUN apt-get install -y ros-kinetic-rviz

#Install multirobot_map_merge_tests package
#RUN git clone https://github.com/fitter22/multirobot_map_merge_tests.git

#Configure environment
CMD ["/bin/bash", "entrypoint.sh"]


# To run that img
#xhost +local:root
#docker run -it -e DISPLAY -e QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix:rw --device /dev/dri -it --rm <name of img>
#xhost -local:root
