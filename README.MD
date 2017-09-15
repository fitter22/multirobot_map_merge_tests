Package multirobot_map_merge_tests is based on turtlebot_gazebo. It creates a sample scene in Gazebo and spawns two turtlebots with slam_gmapping.
To run it: "roslaunch multirobot_map_merge_tests spawn_two_turtlebots.launch"
To controll robot launch "keyboard_teleop_turtleX".

Robots publish two map topics - turtle1/map and turtle2/map.
They can be merged into one map with multirobot_map_merge package (http://wiki.ros.org/multirobot_map_merge).
That package automatically register itself to turtle/map topics and publish map_merge/map.

IMPORTANT:
Map is merged correctly only with confidence > 1. You can check that parameter in map_merge logs. If it's lower map is not merged.

To simultaneously run two replays:
- run: "rosparam set use_sim_time true"
- edit: bag_player/play_two_bags_sync.launch and change the bagfiles patch into correct one
- run: "roslaunch multirobot_map_merge_tests bag_player/play_two_bags_sync.launch"
