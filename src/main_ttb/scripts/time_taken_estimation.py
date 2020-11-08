#Code to estimate approx time taken for robot to scan floorplan 

import math

# Speed parameters
linear_vel = 0.05  # m/s
angular_vel = 0.5  # rad/s

# ---------------------------------------------- HARDCODED PATH APPROACH (START)---------------------------------------------- #
# # Room parameters
# length = 2.0  # metres #Straight forward path
# breadth = 2.0  # metres #Straight path but for turning

# #Path parameters
# dist_from_wall = 0.1 #metres 
# dist_between_path = 0.3

# # Number of full lengths to be travelled
# num_short_straight_paths = (breadth - 2*dist_from_wall)/dist_between_path
# num_long_straight_paths = num_short_straight_paths + 1
# num_turns = 2 * num_short_straight_paths 
# dist_long_straight = length - 2*dist_from_wall

# #Calculation 
# time_taken_straight = (dist_long_straight/linear_vel)*num_long_straight_paths + (dist_between_path/linear_vel)*num_short_straight_paths #seconds
# time_taken_turn = math.pi/(2*angular_vel) * num_turns #seconds
# time_taken_total = time_taken_straight + time_taken_turn #seconds

# ---------------------------------------------- HARDCODED PATH APPROACH (END)---------------------------------------------- #


# ---------------------------------------------- HARDCODED PATH APPROACH (START)---------------------------------------------- #

#Path parameters
length_long = 1.0
length_short = 0.2
num_long = 1
num_short = 0
num_turn = 0

#Calculation 
time_taken_straight = (length_long/linear_vel)*num_long + (length_short/linear_vel)*num_short #seconds
time_taken_turn = math.pi/(2*angular_vel) * num_turn #seconds
time_taken_total = time_taken_straight + time_taken_turn #seconds

# ---------------------------------------------- HARDCODED PATH APPROACH (END)---------------------------------------------- #



def convert(seconds): 
    min, sec = divmod(seconds, 60) 
    hour, min = divmod(min, 60) 
    return "%d hrs %02d mins %02d seconds" % (hour, min, sec)

time_taken_straight = convert(time_taken_straight)
time_taken_turn = convert(time_taken_turn)
time_taken_total = convert(time_taken_total)
 
print('time_taken_straight: ' + str(time_taken_straight))
print('time_taken_turn: ' + str(time_taken_turn))
print('time_taken_total: ' + str(time_taken_total))