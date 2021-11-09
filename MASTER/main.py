import os
import argparse

from CreateCsv import combined_csv
from CreateVideos import ImagesToVideo
from Upload_AWS import upload_csv_aws, upload_video_aws


# CLI Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument(
        "ride_path",
        help="Ride path: Directory where ride's rosbags is extracted to"
    )
args = parser.parse_args()


#current working directory
working_dir = ''

#Sanity check for correctness of CLI argument
if args.ride_path[0] != '/':
	working_dir = '/'+args.ride_path
else:
	working_dir = args.ride_path

if working_dir.endswith('/'):
    working_dir = working_dir[:-1]


#Defining config dictionary for videos
config = {
    "ride_path":working_dir,
    "csv_name":"combined_csv.csv",
    "col_list":[
        "timestamp",
        "zed2",
        '/gps_pos/vehicle_roll',
        '/gps_pos/speed3D',
        ]
    }


# calling appropriate functions and classes
# combined_csv(working_dir)
# ImagesToVideo(config).ride_videos()
upload_csv_aws(working_dir)
upload_video_aws(working_dir)