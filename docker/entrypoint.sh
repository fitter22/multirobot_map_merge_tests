#!/bin/bash
set -e

source /opt/ros/kinetic/setup.bash

mkdir src

cd src

git clone https://github.com/turtlebot/turtlebot_simulator.git

git clone https://github.com/fitter22/multirobot_map_merge_tests.git

cd ..

catkin_make

source /catkin_ws/devel/setup.bash

export TURTLEBOT_GAZEBO_WORLD_FILE="~/catkin_ws/src/turtlebot_simulator/turtlebot_gazebo/worlds/playground.world"

roslaunch multirobot_map_merge_tests spawn_two_turtlebots.launch

exec "$@"
