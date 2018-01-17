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
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/us-robot/catkin_ws/src/ur5-master/universal_robot-kinetic-devel/ur_driver"

# snsure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/us-robot/catkin_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/us-robot/catkin_ws/install/lib/python2.7/dist-packages:/home/us-robot/catkin_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/us-robot/catkin_ws/build" \
    "/usr/bin/python" \
    "/home/us-robot/catkin_ws/src/ur5-master/universal_robot-kinetic-devel/ur_driver/setup.py" \
    build --build-base "/home/us-robot/catkin_ws/build/ur5-master/universal_robot-kinetic-devel/ur_driver" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/us-robot/catkin_ws/install" --install-scripts="/home/us-robot/catkin_ws/install/bin"
