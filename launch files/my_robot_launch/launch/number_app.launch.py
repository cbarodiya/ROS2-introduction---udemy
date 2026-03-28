from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    number_pubisher = Node(
        package="my_py_pkg",
        executable="number_publisher"
    )

    number_counter = Node(
        package="my_cpp_pkg",
        executable="number_counter"
    )

    ld.add_action(number_pubisher)
    ld.add_action(number_counter)

    return ld
