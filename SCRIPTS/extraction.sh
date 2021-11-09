#!/bin/bash


USERID=$1
echo $USERID
RIDEID=$2
echo $RIDEID
BAG_DIR="/srv/beegfs02/scratch/aegis_guardian/data/NEW_BACKEND/$USERID/$RIDEID"
echo $BAG_DIR


/home/user/miniconda/bin/activate bag_extract

source /opt/ros/melodic/setup.bash

cd /app/rosbag_extractor/scripts


for bag_path in $BAG_DIR/*.bag;
do
    subdir=${bag_path%%.*}
    echo "$subdir"
    if [-d "$subdir"]
    then
        echo "directory already exist"
    else
        echo "making dir $subdir"
        mkdir -p "$subdir"
    fi

    ./bag_csv -b $bag_path -o ${subdir} -e /tf /tf_static /UFLD/lanes /UFLD/objects /optimal_path/path_info
done