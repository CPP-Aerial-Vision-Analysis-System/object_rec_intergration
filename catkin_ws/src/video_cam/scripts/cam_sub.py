#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

subscriberNodeName = 'camera_sensor_subscriber'
topicName = "video"

def callbackFunction(message):
    bridgeObject = CvBridge()
    rospy.loginfo("receieve video message")
    convertedFrameBackToCV = bridgeObject.imgmsg_to_cv2(message)
    cv2.imshow("camera",convertedFrameBackToCV)
    cv2.waitKey(1)

rospy.init_node(subscriberNodeName, anonymous = True)
rospy.Subscriber(topicName, Image, callbackFunction)
rospy.spin()
cv2.destroyAllWindows