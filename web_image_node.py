#!/usr/bin/env python3
import cv2
import base64
import simplejpeg
import numpy as np
from sensor_msgs.msg import Image
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge


class WebImageNode(Node):
    """
    Create an ImagePlubisher class, which is a subclass of the Node class.
    """

    def __init__(self):
        """
        Class constructor to set up the node
        """
        # Initiate the Node class's constructor and giv it a name
        super().__init__("web_image_node")
        # self.get_logger().info("Hello from OpenCV!")
        # Create the publisher. This publisher will publish an Image
        # to the web_image topic. The queue size is 10 messages.
        self.publisher_ = self.create_publisher(Image, "web_image", 10)

        # We will publish a message every 0.1 seconds
        timer_period = 0.1  # seconds

        # Create the timer
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # Create a VideoCapture object
        # The argument '0' gets the default webcam.
        self.cap = cv2.VideoCapture(0)

        # Used to convert between ROS and OpenCV images
        self.br = CvBridge()

    def timer_callback(self):
        """
        Callback function.
        This function gets called every 0.1 seconds.
        """
        # Capture frame-by-frame
        # This method returns True/False as well
        # as the video frame.

        ret, frame = self.cap.read()

        if ret == True:

            # Publish the image.
            # The 'cv2_to_imgmsg' method converts an OpenCV
            # image to a ROS 2 image message
            self.publisher_.publish(self.br.cv2_to_imgmsg(frame))
        # Display the message on the console
        self.get_logger().info("Publishing video frame")


def main(args=None):

    # Initialize the rclpy library
    rclpy.init(args=args)

    # Create the node
    web_image_node = WebImageNode()

    # Spin the node so the callback function is called.
    rclpy.spin(web_image_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)

    web_image_node.destroy_node()

    # Shutdown the ROS client library for Python
    rclpy.shutdown()


if __name__ == '__main__':
    main()
