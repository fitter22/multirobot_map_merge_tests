To start gazebo with two independend turtlebots:
- copy files from turtlebot_gazebo folder into corresponding folders in turtlebot_gazebo ROS package
- run: roslaunch turtlebot_gazebo spawnTwoTurtlebots.launch

To simultaneously run two replays:
- run: rosparam set use_sim_time true
- edit: bag_player/play_two_bags_sync.launch and change the launchfiles patch into correct one
- run: roslaunch <package_where_you_placed_that_file> play_two_bags_sync.launch

