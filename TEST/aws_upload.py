import os
import glob
import argparse
import requests
import pandas as pd

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

# print(working_dir.split('/')[-2])

#change directory to working directory
os.chdir(working_dir)

def upload_aws(working_dir):

    #read csv to get the timestamp
    data = pd.read_csv('combined_csv',usecols=['timestamp','zed2'])

    # defining integer key and timestamp
    # integer_key = working_dir.split('/')[-2]
    integer_key = 123459
    timestamp = int(data['timestamp'][0])
    timestamp = 1617121265
    print(timestamp)

    # AWS get request
    # csv_upload_url = 'http://3.251.25.174:8000/statistics/csv-cloud/'+str(timestamp)+'/'+str(integer_key)
    video_upload_url = 'http://3.251.25.174:8000/statistics/video-cloud/'+str(timestamp)+'/'+str(integer_key)

    #sending csv file to AWS
    # csv_data = { 'csv': 'combined_csv.csv' }
    # csv_files = { 'csv': open('combined_csv.csv', 'rb') }
    # r = requests.post(csv_upload_url, data=csv_data, files=csv_files)
    # print("status", r.status_code)

    # sending video files to AWS
    video_list = [i for i in glob.glob('**/*.mp4',recursive=True)]
    print(video_list)

    for video in video_list:
        video_data = {'video':video}
        video_files = {'video':open(video,'rb')}
        r = requests.get(video_upload_url, data=video_data, files=video_files)
        print(video)


    print(timestamp)

# upload_aws(working_dir)