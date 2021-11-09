import re
import ffmpeg
import pandas as pd



#Python function to sort the image paths
def sorted_alphanumeric(data):
    '''
    Python function to returns a sorted array, list,
    series object, tuple etc.
    params: data: A list, series object, list, tuple etc
    '''
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]

    return sorted(data, key=alphanum_key)



#Python class for creating videos
class ImagesToVideo:
    """
    A class to create videos from images

    '''
    Attributes
    ----------
    config: dict
        key value pair dictionary containing ride path, 
        column list to use and name of csv file
    Methods
    -------
    ride_videos():
        generates videos of interesting locations from the ride
    """

    def __init__(self,config):
        """
        Constructs all the necessary attributes for the ImageToVideo
        object.

        Params:
        ------
            config: dict
                key value pair dictionary containing ride path, 
                column list to use and name of csv file
        """
        self.config = config
        self.integer_key = self.config['ride_path'].split('/')[-2]
        self.data = pd.read_csv(
            self.config["ride_path"]+'/'+self.config["csv_name"],
            usecols=self.config["col_list"]
            )

        print(self.data.columns)

        # self.data[self.config['col_list'][2]] = float(self.data[
        #     self.config['col_list'][2]*1e-5
        #     ])

        self.index_origin = 0
        self.start_ride_time = int(self.data[
            self.config['col_list'][0]
            ].loc[0])


        self.index_top_speed = self.data[
            self.data[
                self.config['col_list'][3]
                ] == max(
                    self.data[self.config['col_list'][3]]
                )
            ].index[0]
        self.top_speed_time = int(self.data[
            self.config['col_list'][0]
            ].loc[self.index_top_speed])


        self.index_roll_left = self.data[
            self.data[
                self.config['col_list'][2]
                ] == min(
                    self.data[self.config['col_list'][2]]
                )
            ].index[0]
        self.roll_left_time = int(self.data[
            self.config['col_list'][0]
            ].loc[self.index_roll_left])


        self.index_roll_right = self.data[
            self.data[
                self.config['col_list'][2]
                ] == max(
                    self.data[self.config['col_list'][2]]
                )
            ].index[0]
        self.roll_right_time = int(self.data[
            self.config['col_list'][0]
            ].loc[self.index_roll_right])


        self.index_destination = len(self.data)-1
        self.destination_time = int(self.data[
            self.config['col_list'][0]
            ].loc[self.index_destination])


        self.index_list = {
            self.index_origin : str(self.start_ride_time)+'_'+'start_video.mp4',
            self.index_roll_left : str(self.roll_left_time)+'_'+'left_roll_video.mp4',
            self.index_roll_right : str(self.roll_right_time)+'_'+'right_roll.mp4',
            self.index_top_speed : str(self.top_speed_time)+'_'+'top_speed_video.mp4',
            self.index_destination : str(self.destination_time)+'_'+'destination_video.mp4'
        }

        
    def ride_videos(self):
        """
        Creates 5 videos from the ride data with the images.

        Params:
        -------
            None
        Returns
        -------
            None
        """
        print(self.index_list)
        for key in self.index_list:
            stream_imgs = []
            stream_range = pd.DataFrame()

            if len(self.data) <= 240:
                stream_range = self.data
            elif key - 120 <= 0:
                stream_range = self.data.loc[0:key + 240]
            elif key + 120 >= len(self.data):
                stream_range = self.data.loc[key - 240:]
            else:
                stream_range = self.data.loc[key - 120: key + 120]


            for image_path in sorted_alphanumeric(stream_range[self.config['col_list'][1]]):
                stream_imgs.append(image_path)


            video_writer = ffmpeg.input(
                'pipe:',r='24', f='jpeg_pipe'
                ).output(
                    self.config["ride_path"]+'/'+self.integer_key+'_'+self.index_list[key],
                    vcodec='libx264'
                    ).overwrite_output().run_async(pipe_stdin=True)


            for image_dir in stream_imgs:
                with open(image_dir,'rb') as f:
                    image_data = f.read()
                    video_writer.stdin.write(image_data)

            video_writer.stdin.close()
            video_writer.wait()