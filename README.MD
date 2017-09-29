# multirobot_map_merge_tests

Package multirobot_map_merge_tests is based on turtlebot_gazebo. It creates a sample scene in Gazebo and spawns two turtlebots with slam_gmapping and navigation stack.
Robots publish two map topics - `turtle1/map` and `turtle2/map`.
They can be merged into one map with [multirobot_map_merge package](http://wiki.ros.org/multirobot_map_merge).
That package automatically register itself to `turtleX/map` topics and publish `map_merge/map`.

### To run it locally:
- `roslaunch multirobot_map_merge_tests spawn_two_turtlebots.launch`
- To control robot launch `keyboard_teleop_turtleX.launch`

I created dockerfiles that contain all needed packages and configuration to run project in PC without ROS. You can also just pull docker image from: `fitter/multirobot_map_merge_tests:latest`
If you want to configure your ros locally in your machine you can find some tips in docker files.

### To run it via docker:
- You can use img from dockerhub or just build one in your machine
- Expose your xhost `xhost +local:root` (the simplest way, but not secure. More info  [here](http://wiki.ros.org/docker/Tutorials/GUI))
- `docker run -it -e DISPLAY -e QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix:rw --device /dev/dri --rm <name of img>` <- for full GUI mode
- or just `docker run -it -e k8s=true --rm <name if img>` <- ""headless"" mode for kubernetes
- When you are done dont forget about `xhost -local:root`

### To simultaneously run two replays:
- `rosparam set use_sim_time true`
- edit `bag_player/play_two_bags_sync.launch` and change the bagfiles patch into correct one
- `roslaunch multirobot_map_merge_tests bag_player/play_two_bags_sync.launch`

## IMPORTANT:
Map is merged correctly only with confidence > 1. You can check that parameter in map_merge logs. If it's lower map is not merged.
