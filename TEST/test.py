import os
import glob
import argparse
import requests

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

print(working_dir.split('/')[-2])

os.chdir(working_dir)

timestamp = 32143254334
integer_key = 446546

# #URL for file uploads
# csv_upload_url = 'http://3.251.25.174:8000/statistics/csv-cloud/' +str(timestamp)+ '/' +str(integer_key) 
video_upload_url = 'http://3.251.25.174:8000/statistics/csv-cloud/' +str(timestamp) + '/' +str(integer_key) 

# print(csv_upload_url)
# csv_data = { 'csv': 'combined_csv.csv' }
# csv_files = { 'csv': open('combined_csv.csv', 'rb') }



video_list = [i for i in glob.glob('**/*.mp4',recursive=True)]
print(video_list)

for video in video_list:
    video_data = {'video':video}
    video_files = {'video':open(video,'rb')}
    r = requests.get(video_upload_url, data=video_data, files=video_files)
    print(video)

'/srv/beegfs02/scratch/aegis_guardian/data/rosbags/SA_amalitech/Ride002'

# print("before post request")
# try:
#     r = requests.get(csv_upload_url, data=csv_data, files=csv_files)
# except:
#     pass 
