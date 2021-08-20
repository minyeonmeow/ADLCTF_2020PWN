#!/bin/bash

project_root=$PWD

if [ "$1" = "up" ]
then
    arg="up -d --build"
elif [ "$1" = "down" ]
then
    arg="$1"
else
    echo "usage: sudo ./setup_all_container.sh up|down"
    exit
fi

for d in $project_root/*/;do
    project_name=`basename $d`
    if [ -e "$d/docker" ]
    then
        cd $d/docker
        sudo docker-compose -p $project_name $arg
    fi
done
