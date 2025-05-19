import os 
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():

    robotXacroName="robot"
    namePackage="my_bot"

    modelFileRelativePath="description/robot.urdf.xacro"
    pathModelFile = os.path.join(get_package_share_directory(namePackage),modelFileRelativePath)
    worldFileRelativePath="worlds/box_world.sdf"
    pathWorldFile= os.path.join(get_package_share_directory(namePackage),worldFileRelativePath)
    
    rvizRelativePath='config/view.rviz'
    rviz_config_path=os.path.join(get_package_share_directory(namePackage),rvizRelativePath)

    robotDescription=xacro.process_file(pathModelFile).toxml()

    gazebo_rosPackageLaunch=PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('ros_gz_sim'),'launch','gz_sim.launch.py'))

    gazeboLaunch=IncludeLaunchDescription(gazebo_rosPackageLaunch,launch_arguments={'gz_args':[f"{pathWorldFile} -r"],'on_exit_shutdown':'true'}.items())


    spawnModelNodeGazebo=Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-name',robotXacroName,'-topic','robot_description'],
        output='screen',
    )

    nodeRobotStatePublisher=Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robotDescription,'use_sim_time':True}]
    )

    bridge_params=os.path.join(get_package_share_directory(namePackage),'parameters','bridge_parameters.yaml')

    start_gazebo_ros_bridge_cmd=Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['--ros-args','-p',f'config_file:={bridge_params}'],
        output='screen'
    )

    rviz2=Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d',rviz_config_path])
    
    '''map_tf=Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="odom_to_base_footprint_broadcaster",
        arguments=['0','0','0','0','0','0','1','map','odom']
    )'''

    LaunchDescriptionObject=LaunchDescription()

    LaunchDescriptionObject.add_action(gazeboLaunch)

    LaunchDescriptionObject.add_action(spawnModelNodeGazebo)
    LaunchDescriptionObject.add_action(nodeRobotStatePublisher)
    LaunchDescriptionObject.add_action(start_gazebo_ros_bridge_cmd)
    LaunchDescriptionObject.add_action(rviz2)
    #LaunchDescriptionObject.add_action(map_tf)

    return LaunchDescriptionObject
        