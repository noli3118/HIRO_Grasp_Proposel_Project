#! /usr/bin/env python3
import franka_gripper.msg
import rospy
import sys
import actionlib
from std_msgs.msg import Float32MultiArray


class hiro_grasp:
    def __init__(self):
        print("Right before open call")
        self.open()

    def __set_open_grasp(self):
        self.__width = 0.1
        self.__inner = 0.020
        self.__outer = 0.020
        self.__speed = 0.1
        self.__force = 10

    def grasp(self):
        print('create client')
        client = actionlib.SimpleActionClient('/franka_gripper/grasp', franka_gripper.msg.GraspAction)
        print('wait for client')
        # client.wait_for_server()
        goal = franka_gripper.msg.GraspGoal()
        goal.width = self.__width
        goal.epsilon.inner = self.__inner
        goal.epsilon.outer = self.__outer
        goal.speed = self.__speed
        goal.force = self.__force
        print('send goal')
        client.send_goal(goal)
        # client.wait_for_result()
    
    def open(self):
        self.__set_open_grasp()
        self.grasp()
    
    def set_grasp_width(self, width):
        self.__width = width

if __name__ == '__main__':
    # rospy.init_node('grasp_test')
    hiro_g = hiro_grasp()
