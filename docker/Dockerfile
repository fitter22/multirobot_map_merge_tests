FROM ros:kinetic-ros-base

# Kubernetes mode enable env variable
# defaul (false) means Gazebo will run with GUI
ENV k8s false

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y git

# Set the default directory where CMD will execute
WORKDIR /catkin_ws

ADD . /catkin_ws

# Install gezebo
RUN apt-get install -y \
  ros-kinetic-gazebo-ros-pkgs \
  ros-kinetic-gazebo-ros-control \
  ros-kinetic-kobuki-gazebo-plugins \
  ros-kinetic-gazebo-plugins

# Install turtlebot packages
RUN apt-get install -y \
  ros-kinetic-turtlebot-description \
  ros-kinetic-turtlebot-bringup \
  ros-kinetic-turtlebot-navigation \
  ros-kinetic-turtlebot-teleop

# Install rviz
RUN apt-get install -y ros-kinetic-rviz

# Install additional packages
RUN apt-get install -y ros-kinetic-tf2-geometry-msgs

# Clone repos
RUN mkdir src \
  && cd src \
  && git clone https://github.com/turtlebot/turtlebot_simulator.git \
  && git clone https://github.com/fitter22/multirobot_map_merge_tests.git \
  && git clone https://github.com/hrnr/m-explore.git

# Configure environment
CMD ["/bin/bash", "entrypoint.sh"]
