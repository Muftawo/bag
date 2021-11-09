#!/bin/sh
USERID="SA_amalitech"
RIDEID="Ride002"
BAG_DIR="/srv/beegfs02/scratch/aegis_guardian/data/rosbags/$USERID/$RIDEID/"
# check="/srv/beegfs02/scratch/aegis_guardian/data/rosbags/SA_amalitech/Ride001/"
# echo $BAG_DIR

# ls $BAG_DIR

for bag_path in $BAG_DIR*.bag;
do
    echo "$bag_path"
  
    subdir=${bag_path%%.*}
    echo "$subdir"
    # echo "finish"


    if [ -d "$subdir"]
    then
        echo "directory already exist"
    else
        echo "making dir $subdir"
        mkdir -p "$subdir"
    fi

done

echo "Over"