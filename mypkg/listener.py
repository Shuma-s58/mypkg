# SPDX-FileCopyrightText: 2022 Shuma Suzuki
# SPDX-LIcense-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener():
    def __init__(self):
        self.sub = node.create_subscription(Int16, "countup", cb, 10)

    def cb(self, msg):
        #global node
        self.node.get_logger().info("Listen: %d" % msg.data)

def main():
    rclpy.init()
    node = Node("listener")
    listener = Listener()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
