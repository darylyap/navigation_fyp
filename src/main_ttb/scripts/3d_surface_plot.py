import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
import math

##Initialisation

#Trial 2
# x_range = 3
# y_range = 5

#Trial 3
x_range = 4
y_range = 6 
total_sample = y_range * x_range

array = []
data = []

dist = 200 #Distance between readings (mm)

#Conversion
pix_res = 0.052
spirit_bubble_res = 0.5
pix_deg_conversion = 0.5 * 0.052

#Define 3D plot
fig = plt.figure()
ax = fig.gca(projection='3d', adjustable='box')

# Create  meshgrid  
X = np.arange(1, x_range+1)
Y = np.arange(1, y_range+1)
X, Y = np.meshgrid(X,Y)
X = 200*X.transpose()
Y = 200*Y.transpose()
##print(X)
##print(Y)

#Create x,y coord vals
for j in range(1,x_range+1):
  for k in range(1,y_range+1):
    array = np.append(array,[j,k], axis=0)
array = np.reshape(array,(total_sample,2))
##print(array)
x = array[:,0]
y = array[:,1]
##print(x)
##print(y)
 
#Data values
#Take bottom left as (0,0) coords --> similar to graph coords

#Trial 2 values
# val = np.array\
#  ([[9.6,	-110.9],
#  [-8.87,	-78.13],
#  [-18.8,	-11.06],
#  [-23.47, 51.1],
#  [-7.73,	60.7],
#  [11.7,	-101.8],
#  [22.9,	-89.1],
#  [10.9,	-2.5],
#  [4.73,	53.3],
#  [-6.8,	60],
#  [10.7,	-118.1],
#  [42.9,	-79.6],
#  [53.7,	0.93],
#  [38.3,	61.3],
#  [-1.7,	67.9]])

#Trial 3 values
#X: Positive value = RIGHT is raised
#Y: Positive value = BACK is raised
val = np.array\
([[1.6,	31.93],
[19.27,	47.13],
[52.07,	-12.73],
[55.13,	15.67],
[0,	43.87],
[-4.67,	13.8],
[9.67,	34.07],
[47.93,	25],
[62.93,	-10.53],
[50,	11.6],
[68.2,	67.87],
[97.87,	-21.73],
[58.8,	1.67],
[54,	16.8],
[49.6,	22.93],
[48.93,	-7.73],
[38.53,	22.47],
[13.4,	-13.73],
[56.27,	-0.27],
[83.27,	-1.87],
[53.67,	11.4],
[64.27,	39.8],
[57.6,	-7.8],
[70.6,	-3.73]])

#Convert pixel del to rad
val = val * pix_deg_conversion * math.pi/180

val_x = val[:,0]
val_y = val[:,1]
val_x = np.reshape(val_x,(x_range,y_range))
val_y = np.reshape(val_y,(x_range,y_range))
##print('val_x')
##print(val_x)
##print('val_y')
##print(val_y)

##Height data for each point
#Initate array with zeroes
height = np.zeros((x_range,y_range))
base_array = np.zeros((x_range,1))

#Init values
height[0][0] = 0
height_counter_x = 0

#Create new inclination array (rad) used for height calculations [=(dist/2)*sin_theta]
#result gives height diff in mm
val_x_tan = (dist/2) * np.tan(np.absolute(val_x))
val_y_tan = (dist/2) * np.tan(np.absolute(val_y))
# print("val_x_tan")
# print(val_x_tan)
##print("val_y_tan")
##print(val_y_tan)


#FOR TRIAL 2, sign = -1
sign = 1

#Get first column value (horizontal adding)
for k in range(1,x_range):
  del_height_init_x = (val_x_tan[k][0] * np.sign(val_x[k][0])) + (val_x_tan[k-1][0] * np.sign(val_x[k-1][0]))
  height[k][0] = height_counter_x + del_height_init_x * sign
  height_counter_x = height[k][0]
  # print("del_height_init_x")
  # print(del_height_init_x)
# print("height 1")
# print(height)

#Get first row value (vertical adding)
for q in range(1,y_range):
  if q == 1:
  	height_counter_y = 0 
  del_height_init_y = (val_y_tan[0][q-1] * np.sign(val_y[0][q-1])) + (val_y_tan[0][q] * np.sign(val_y[0][q]))
  height[0][q] = height_counter_y - del_height_init_y * sign
  height_counter_y = height[0][q]
  # print("del_height_init_y")
  # print(del_height_init_y)
# print("height 2")
# print(height)

# from_x = np.copy(height)
# from_y = np.copy(height)


#Get subsequent row values (vertical + horz adding)
for i in range(1,x_range):
  for j in range(1,y_range):
    del_height_x = (val_x_tan[i-1][j] * np.sign(val_x[i-1][j])) + (val_x_tan[i][j] * np.sign(val_x[i][j]))
    del_height_y = (val_y_tan[i][j-1] * np.sign(val_y[i][j-1])) + (val_y_tan[i][j] * np.sign(val_y[i][j]))
    # from_x[i][j] = from_x[i-1][j] + del_height_x * sign
    # from_y[i][j] = from_y[i][j-1] - del_height_y * sign
    height[i][j] = ((height[i-1][j] + del_height_x * sign) + (height[i][j-1] - del_height_y * sign))/2

# diff_array = (np.subtract(from_x,from_y))


# print('from_x')
# print(from_x)
# print('from_y')
# print(from_y)
# print("diff_array")
# print(diff_array)
print("height")
print(height)

Z = height


# #Plot the surface
# surf = ax.plot_surface(X, Y, from_x, cmap=cm.bwr, alpha=0.8)
# surf = ax.plot_surface(X, Y, from_y, cmap=cm.binary, alpha=0.8)
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha=0.4)


#Contour of surface plot
cset = ax.contour(X, Y, Z, total_sample, zdir='z', offset = -13, cmap=cm.coolwarm) #[offset] Trial 2:-18; Trial 3:-13
# cset = ax.contour(X, Y, Z, total_sample, zdir='z', offset = -18, cmap=cm.coolwarm)
#cset = ax.contourf(X, Y, Z, 12, zdir='z', offset = -0.25, cmap=cm.coolwarm)

##Configure plot
#Indicate position number
position_idx = np.arange(1,total_sample+1)
#print(position_idx)
for i, txt in enumerate(position_idx):
	ax.text(dist*x[i],dist*y[i],-12.5,position_idx[i], color = 'green', alpha = 0.4) #[Z-axis] Trial 2:-15 ; Trial 3:-12.5
	# ax.text(dist*x[i],dist*y[i],-15,position_idx[i], color = 'green', alpha = 0.4) 

plt.xticks(np.arange(dist*min(x), dist*max(x)+1, dist))
plt.yticks(np.arange(dist*min(y), dist*max(y)+1, dist))
# plt.xticks(x,"")
# plt.yticks(y,"") 
# plt.gca().set_aspect('equal', adjustable='box')
fig.colorbar(surf, shrink=0.8)
plt.show()
