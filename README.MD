Package multirobot_map_merge_tests is based on turtlebot_gazebo. It creates a sample scene in Gazebo and spawns there two turtlebots.
To run it: roslaunch multirobot_map_merge_tests spawnTwoTurtlebots.launch

To simultaneously run two replays:
- run: rosparam set use_sim_time true
- edit: bag_player/play_two_bags_sync.launch and change the launchfiles patch into correct one
- run: roslaunch multirobot_map_merge_tests bag_player/play_two_bags_sync.launch

