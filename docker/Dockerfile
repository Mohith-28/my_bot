# ROS 2 Jazzy + Gazebo Harmonic environment for my_bot (Ubuntu 24.04 base)
FROM osrf/ros:jazzy-desktop

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
        ros-jazzy-ros-gz \
        ros-jazzy-xacro \
        ros-jazzy-robot-state-publisher \
        ros-jazzy-joint-state-publisher \
        ros-jazzy-joint-state-publisher-gui \
        ros-jazzy-teleop-twist-keyboard \
        ros-jazzy-slam-toolbox \
        ros-jazzy-nav2-map-server \
        ros-dev-tools \
        mesa-utils \
    && rm -rf /var/lib/apt/lists/*

# The base image already has user "ubuntu" with uid/gid 1000, matching the host user,
# so files written into the mounted workspace stay owned by you.
RUN echo 'source /opt/ros/jazzy/setup.bash' >> /home/ubuntu/.bashrc \
 && echo '[ -f /ws/install/setup.bash ] && source /ws/install/setup.bash' >> /home/ubuntu/.bashrc

USER ubuntu
WORKDIR /ws
CMD ["bash"]
