# SPDX-FileCopyrightText: 2022 Shuma Suzuki
# SPDX-LIcense-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

#def cb(node, msg):
    #global node
    #node.get_logger().info("Listen: %d" % msg.data)

class Listener():
    #def cb(self, msg):
        #global node
        #self.node.get_logger().info("Listen: %d" % msg.data)

    def __init__(self):
        self.sub = node.create_subscription(Int16, "countup", cb, 10)

    def cb(msg):
        #global node
        node.get_logger().info("Listen: %d" % msg.data)


rclpy.init()
node = Node("listener")
listener = Listener(msg)
rclpy.spin(node)
