## Robot Package Template

This GitHub repository consists of the files that will be required to build a two wheeled mobile robot that works based on a differential drive system and contains a LiDAR for autonomous navigation in the given world using the ROS2,Gazebo simualator and Rviz2 viasualizer.

The basic template of this repo was provided by @JoshNewans(youtube: Articulated Robot) and I modified this repository in such a way that it can be used for building and simulating a mobile robot in the ROS2 Jazzy and Gazebo Harmonic simulator. The tutorials taught by JoshNewans is really great and since he is teaching using the ROS2 Foxy and Gazebo Classic, I am providing this reposiotry as the template for the people who are using the ROS2 Jazzy or Gazebo harmonic to follow along with the tutorials and understand the modifications made. 

This is a GitHub template. You can make your own copy by clicking the green "Use this template" button.

It is recommended that you keep the repo/package name the same, but if you do change it, ensure you do a "Find all" using your IDE (or the built-in GitHub IDE by hitting the `.` key) and rename all instances of `my_bot` to whatever your project's name is.

Note that each directory currently has at least one file in it to ensure that git tracks the files (and, consequently, that a fresh clone has direcctories present for CMake to find). These example files can be removed if required (and the directories can be removed if `CMakeLists.txt` is adjusted accordingly).
