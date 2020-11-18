#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import String, Float32
from turtlesim.msg import Pose


def pose_callback(pose):
    #Theta: -pi<theta<pi
    rospy.loginfo(rospy.get_caller_id() + " %.2f ", pose.theta)

def xy_callback(data):
    global temp_array
    temp_array.append(data)

def segment_array():
    global temp_array
    global combi_array

    combi_array.append(temp_array)
    temp_array = []

def straight(dist, linear_vel, vel_msg, velocity_publisher, distance_publisher, time_publisher):

    print("Going straight for " + str(dist) + " m")

    vel_msg.linear.x = linear_vel

    t0 = rospy.Time.now().to_sec()
    current_distance = 0

    while(current_distance < dist):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance = linear_vel*(t1-t0)
        # distance_publisher.publish(current_distance)
        # time_publisher.publish(t1-t0)
        # print(t1-t0, current_distance)

    vel_msg.linear.x = 0

    print('STOP!!')
    velocity_publisher.publish(vel_msg)
    rospy.Rate(1).sleep()

    return None


def turn_90(turn_right, angular_vel, vel_msg, velocity_publisher, distance_publisher, time_publisher):

    print("Turning 90 degrees")

    if (turn_right == True):
        vel_msg.angular.z = -angular_vel
    else:
        vel_msg.angular.z = angular_vel

    current_angle = 0
    t0 = rospy.Time.now().to_sec()

    while(current_angle < (math.pi/2)):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = abs(angular_vel)*(t1-t0)
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    # rospy.Rate(10).sleep()

    return None


def move():
    # Starts a new node
    rospy.init_node('movement_node', anonymous=True)
    # velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)  # to test on turtlesim
    # launch with roscore & rosrun turtlesim turtlesim_node & python3 movement_node.py
    # distance_publisher = rospy.Publisher('/dist_travel', Float32, queue_size=10)
    # time_publisher = rospy.Publisher('/time_travel', Float32, queue_size=10)
    # segment_break_publisher = rospy.Publisher('/segment_break', String, queue_size=10)
    # end_message_publisher = rospy.Publisher('/end_message', String, queue_size=10)

    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    rospy.Subscriber('/xy_pos', Int64MultiArray, xy_callback)

    rate = rospy.Rate(1)  # 10hz
    vel_msg = Twist()

    # Init array
    temp_array = []
    combi_array = []

    # Desired parameters
    linear_vel = 1  # m/s
    angular_vel = 1  # rad/s
    linear_distance = 2  # metres #Straight forward path
    horizontal_distance = 0.5  # metres #Straight path but for turning

    # Number of full length travelled as defined by dist = 'linear_distance'
    num_straight_paths = 2

    # Direction of first turn after first straight path. Right = True, Left = False
    turn_right = False

    # Init parameters
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    straight_count = 0
    turn_count = 0
    desired_turn_count = num_straight_paths - 1

    while not rospy.is_shutdown():

        while straight_count != num_straight_paths:

            # Straight path [LINEAR]
            straight(linear_distance, linear_vel, vel_msg,
                     velocity_publisher, distance_publisher, time_publisher)
            straight_count += 1

            # Turning
            if (turn_count < desired_turn_count):
                turn_90(turn_right, angular_vel, vel_msg,velocity_publisher, distance_publisher, time_publisher)
                # segment_break_publisher.publish('seg_break')
                segment_array()
                straight(horizontal_distance, linear_vel, vel_msg, velocity_publisher,distance_publisher, time_publisher)  # Straight path [HORIZONTAL]
                # segment_break_publisher.publish('seg_break')
                segment_array()
                turn_90(turn_right, angular_vel, vel_msg,velocity_publisher, distance_publisher, time_publisher)
                turn_count += 1
                turn_right = not turn_right

        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)
        end_message_publisher.publish('end')
        print('End of path')
        rate.sleep()
        break

-------------------
def callback(data):
    #Theta: -pi<theta<pi
    global segment
    if (data == 'seg_break'):
        segment = True

    if (segment == True):      
        combi_array.append(temp_array)
        temp_array = []
        segment = False



if __name__ == '__main__':
    try:
        # Testing our function
        move()
    except rospy.ROSInterruptException:
        pass
