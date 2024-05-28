#!/usr/bin/env python

import rospy
import os
import subprocess
# from franka_msgs.srv import StringService, StringServiceResponse
from touch_ar_msgs.srv import StringService, StringServiceResponse

def command_line_callback(request):
    rospy.loginfo("Received request with data: %s", request.data)

    command = f"source /opt/ros/noetic/setup.bash && source {os.path.expanduser('~/Projects/catkin_ws')}/devel/setup.bash && {request.data}"
    try:
        # Execute the command string using shell=True
        result = subprocess.run(command, shell=True, capture_output=True, text=True, executable='/bin/bash')
        response = result.stdout if result.stdout else result.stderr
        rospy.loginfo("Command output: %s", response)
    except subprocess.CalledProcessError as e:
        response = e.stderr
        rospy.logerr("Command failed with CalledProcessError: %s", response)
    except Exception as e:
        response = str(e)
        rospy.logerr("Command failed with Exception: %s", response)
    
    return StringServiceResponse(response)

def string_service_server():
    rospy.init_node('command_line_service_server')
    service = rospy.Service('command_line_service', StringService, command_line_callback)
    rospy.loginfo("String Service Server is ready.")
    rospy.spin()

if __name__ == "__main__":
    string_service_server()
