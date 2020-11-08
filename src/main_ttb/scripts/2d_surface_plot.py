#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32


#Testing for listener
# def callback_dist(data):
#     rospy.loginfo(rospy.get_caller_id() + " %.2f ", data.data)

# def callback_time(data):
#     rospy.loginfo(rospy.get_caller_id() + " %.2f ", data.data)

# def callback_end_message(data):
#     rospy.loginfo(rospy.get_caller_id() + " %s ", data.data)
    
#     # if (data.data == 'end'):
#     # 	plot_visualisation()
    
# def listener():

#     # In ROS, nodes are uniquely named. If two nodes with the same
#     # name are launched, the previous one is kicked off. The
#     # anonymous=True flag means that rospy will choose a unique
#     # name for our 'listener' node so that multiple listeners can
#     # run simultaneously.
#     rospy.init_node('listener', anonymous=True)
#     # rospy.Subscriber("dist_travel", Float32, callback_dist)
#     rospy.Subscriber("time_travel", Float32, callback_time)
#     # rospy.Subscriber("end_message", String, callback_end_message)

#     # spin() simply keeps python from exiting until this node is stopped
#     rospy.spin()

# if __name__ == '__main__':
#     try:
#         listener()
#     except rospy.ROSInterruptException:
#         pass




def plot_visualisation():

	------------------------------RAW DATA--------------
	#Init 

	data_array = []
	file_name = "0.5 1.txt"

	with open(file_name, "r") as file:
		for line in file:
			new_line = line.split(' ')
			data_array = np.append(data_array,[int(new_line[0]),int(new_line[1])], axis=0)
			# data_array.append((new_line[0],new_line[1]))
			# print(new_line[0],new_line[1])

	# print(type(data_array.shape[0]))
	# print(data_array.shape[0])
	data_array = np.reshape(data_array,(data_array.shape[0]//2,2))
	len_data_array = data_array.shape[0]
	# print('len_data_array: ' + str(len_data_array))

	desired_dist_per_reading = 0.05 #m
	ttb_dist_travel = 1.2 #metres
	desired_values = 1 + round(ttb_dist_travel/desired_dist_per_reading)
	# print('desired_values: ' + str(desired_values))

	#Obtain linearly spaced points based on how many 
	idx = np.round(np.linspace(0, len(data_array) - 1, desired_values)).astype(int)
	val = data_array[idx]
	# print(val)
	# print('len_new_sampled_array: ' + str(len(val)))


	#------------------------------------------------------
	## Index vals For plotting purposes

	array = []
	data = []

	##Initialisation
	y_range = 1
	x_range = val.shape[0]
	total_sample = y_range * x_range

	##Init position
	for j in range(1,x_range+1):
	  for k in range(1,y_range+1):
	    array = np.append(array,[j,k], axis=0)
	# print(array)
	array = np.reshape(array,(total_sample,2))
	# print(array)
	# print(array[:,0])
	# print(array[:,1])

	#------------------------------------------------------

	#print(val)
	#print(val[:,0])
	#print(val[:,1])

	# array_arrow_end = np.add(array, val)
	# print("array_arrow_end")
	# print(array_arrow_end)

	x = array[:,0]
	y = array[:,1]
	val_x = val[:,0]
	val_y = val[:,1]
	C = np.sqrt(val_x**2 + val_y**2)
	# print("val_x")
	# print(val_x)
	# print(type(val_x[0]))
	# print("val_y")
	# print(val_y)
	# print(type(val_y))
	# print("C")
	# print(C)

	##Draw arrows
	#kwargs = {'cmap':'RdPu'}
	#quiver([X, Y], U, V, [C], **kw)  
	#--> Where X, Y define the arrow locations, U, V define the arrow directions, and C optionally sets the color
	quiver = plt.quiver(x, y, -val_x, val_y, C, scale = 14000)

	#Set limits of graph plot
	plt.xlim(0.5, x_range + 0.5)
	plt.ylim(0.5, y_range + 0.5)

	#Annotate diagram
	position_idx = np.arange(1,total_sample+1)

	for i, txt in enumerate(position_idx):
		plt.annotate(txt, (x[i], y[i]),xytext = (0.1+x[i], 0.1+y[i]))

	plt.scatter(x, y, marker = 'x')
	plt.gca().set_aspect('equal', adjustable='box')
	plt.colorbar()
	plt.xticks(x,"")
	plt.yticks(y,"") 
	plt.show()
