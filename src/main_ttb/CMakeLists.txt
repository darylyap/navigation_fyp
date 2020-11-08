cmake_minimum_required(VERSION 2.8.3)
project(main_ttb)

find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  geometry_msgs
  image_transport
  message_generation
  nav_msgs
  roscpp
  rospy
  sensor_msgs
  std_msgs
  tf
  actionlib_msgs
)
find_package(OpenCV REQUIRED)

#add_message_files(
#FILES
#)

generate_messages(
  DEPENDENCIES
  actionlib_msgs
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS
  message_runtime
  actionlib_msgs
  cv_bridge
  geometry_msgs
  image_transport
  message_generation
  nav_msgs
  roscpp
  rospy
  sensor_msgs
  std_msgs
  tf
)

include_directories(
include
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)

add_executable(odom scripts/odom.cpp)
target_link_libraries(odom ${catkin_LIBRARIES})
add_dependencies(odom nav_msgs_generate_messages_cpp)

add_executable(talker scripts/talker.cpp)
target_link_libraries(talker ${catkin_LIBRARIES})
add_dependencies(talker std_msgs_generate_messages_cpp)

add_executable(listener scripts/listener.cpp)
target_link_libraries(listener ${catkin_LIBRARIES})
add_dependencies(listener std_msgs_generate_messages_cpp)

