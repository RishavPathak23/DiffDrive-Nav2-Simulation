import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction, RegisterEventHandler
from launch.event_handlers import OnProcessStart
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    ARGUEMENTS = [
        DeclareLaunchArgument(
            'controller_manager_cfg',
            default_value=os.path.join(
                get_package_share_directory('nav2_controller'),
                'config',
                'controllers_manager.yaml'
            ),
            description='Full path to controller manager config file'
        )

    ]

    controller_manager_cfg = LaunchConfiguration('controller_manager_cfg')


    controller_manager_node = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[controller_manager_cfg],
        output='screen'
    )

    ld = LaunchDescription(ARGUEMENTS)
    ld.add_action(controller_manager_node)

    return ld