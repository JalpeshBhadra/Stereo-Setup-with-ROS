
# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
import time 
import num		py as np
from matplotlib import pyplot as plt
# Instantiate CvBridge
bridge = CvBridge()
global i
i=150
global j
j=150


def finddepth():
    if(i!=150 and j!=150):
        print(i,j,'function')
        imgL = cv2.imread('Jalpesh_Left/camera_image_1_'+str(i-1)+'.jpeg',0)
        imgR = cv2.imread('Jalpesh_Right/camera_image_2_'+str(i-1)+'.jpeg',0)
        stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
        disparity = stereo.compute(imgL,imgR)
        print("going")
        cv2.imwrite('Jalpesh_Depth/depth'+str(i-1)+'.jpeg',disparity)

def image_callback(msg):
    print("Received an image1")
    global 
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg 
        time.sleep(2)
        cv2.imwrite('Jalpesh_Left/camera_image_1_'+str(i)+'.jpeg', cv2_img)

 
    finddepth()

    i=i+1

def image_callback_2(msg):
    print("Received an image2")
    global j
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg 
        time.sleep(2)
        cv2.imwrite('Jalpesh_Right/camera_image_2_'+str(j)+'.jpeg', cv2_img)

   



    j=j+1

def main():
    rospy.init_node('image_listener')
    # Define your image topic
    #image_topic = "/usb_cam/image_raw"
    image_topic1= "/camera1/usb_cam1/image_raw"
    image_topic2= "/camera2/usb_cam2/image_raw"
    # Set up your subscriber and define its callback
    print("repeat")
    rospy.Subscriber(image_topic1, Image, image_callback)
    rospy.Subscriber(image_topic2, Image, image_callback_2)
    # Spin until ctrl + c
    rospy.spin()




if __name__ == '__main__':
    main()
