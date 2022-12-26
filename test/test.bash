#!/bin/bash -xv
# SPDX-FileCopyrightText: 2022 Shuma Suzuki
# SPDX-LIcense-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 20 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

ng () {
      echo NG at Line $1
      res=1
}

res=0

### I/O TEST ###

out=$(cat /tmp/mypkg.log | grep -c 'Listen: 10')
[ "${out}" = "1" ] || ng ${LINENO}

### STRANGE INPUT ###

out=$(cat /tmp/mypkg.log | grep -c 'listen: 10')

[ "$?" = 1 ]       || ng ${LINENO}
[ "${out}" = "0" ] || ng ${LINENO} 

