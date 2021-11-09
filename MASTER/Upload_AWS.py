import os
import glob
import requests
import pandas as pd



def upload_csv_aws(working_dir):

    os.chdir(working_dir)
    data = pd.read_csv('combined_csv.csv',usecols=['timestamp','zed2'])

    integer_key = working_dir.split('/')[-2]
    timestamp = int(data['timestamp'][7])
    
    csv_upload_url = 'http://3.251.25.174:8000/statistics/csv-cloud/'+str(timestamp)+'/'+str(integer_key)
    

    csv_data = {'csv':'combined_csv.csv'}
    csv_files = {'csv':open('combined_csv.csv','rb')}
    r = requests.get(csv_upload_url, data=csv_data, files=csv_files)
    print("status", r.status_code)



def upload_video_aws(working_dir):

    os.chdir(working_dir)
    data = pd.read_csv('combined_csv.csv',usecols=['timestamp','zed2'])

    integer_key = working_dir.split('/')[-2]
    timestamp = int(data['timestamp'][7])
    
    video_upload_url = 'http://3.251.25.174:8000/statistics/video-cloud/'+str(timestamp)+'/'+str(integer_key)

    video_list = [i for i in glob.glob('**/*.mp4',recursive=True)]
    

    for video in video_list:
        video_data = {'video':video}
        video_files = {'video':open(video,'rb')}
        r = requests.get(video_upload_url,data=video_data,files=video_files)
        print('status', r.status_code)