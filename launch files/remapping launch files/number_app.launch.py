from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    number_pubisher = Node(
        package="my_py_pkg",
        executable="number_publisher",
        name="my_number_publisher",
        remappings=[("/number", "/my_number")]
    )

    number_counter = Node(
        package="my_cpp_pkg",
        executable="number_counter",
        name="my_number_counter",
        remappings=[("/number", "/my_number")]
    )

    ld.add_action(number_pubisher)
    ld.add_action(number_counter)

    return ld
