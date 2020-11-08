#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/daryl/ttb_ws/src/follow_waypoints"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/daryl/ttb_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/daryl/ttb_ws/install/lib/python2.7/dist-packages:/home/daryl/ttb_ws/build/follow_waypoints/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/daryl/ttb_ws/build/follow_waypoints" \
    "/usr/bin/python2" \
    "/home/daryl/ttb_ws/src/follow_waypoints/setup.py" \
     \
    build --build-base "/home/daryl/ttb_ws/build/follow_waypoints" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/daryl/ttb_ws/install" --install-scripts="/home/daryl/ttb_ws/install/bin"
