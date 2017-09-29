#!/bin/bash
set -e

source /opt/ros/kinetic/setup.bash

catkin_make

source /catkin_ws/devel/setup.bash

export TURTLEBOT_GAZEBO_WORLD_FILE="/catkin_ws/src/turtlebot_simulator/turtlebot_gazebo/worlds/playground.world"

if [ "$k8s" = true ]; then
  roslaunch multirobot_map_merge_tests spawn_two_turtlebots.launch gui:=false
else
  echo $k8s
  roslaunch multirobot_map_merge_tests spawn_two_turtlebots.launch gui:=true
fi

exec "$@"
