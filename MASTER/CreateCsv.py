import os
import glob
import pandas as pd


def combined_csv(ride_path):
    """
    Python function for returning dataframe. The function also creates
    a combined csv if it does not exist.
    
    params: ride_path: this is the path to the specific_user_ride_directory

        returns: Dataframe as a csv file
    """

    if os.path.exists(ride_path):
        extension = 'csv'
        os.chdir(ride_path)
        all_filenames = [i for i in glob.glob('*/*.{}'.format(extension),recursive=True)]

        if os.path.exists("combined_csv.csv"):
            # csv = pd.read_csv("combined_csv.csv")
            # no_to_return = 50
            # no_to_skip = int((len(csv)) / no_to_return)
            # csv = csv.loc[0::no_to_skip]

            return 'combined csv file already exit'

        else:
            df_list = []
            for f in all_filenames:
                current_csv = f
                data = pd.read_csv(current_csv)
                data["zed2"] = os.path.split(f)[0]+'/'+'images'+ data["zed2"]
                df_list.append(data)
    
            combined_df = pd.concat(df_list)
            combined_df = combined_df.sort_values(by='timestamp')
            combined_df.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')

            # csv = pd.read_csv("combined_csv.csv")
            # no_to_return = 50
            # no_to_skip = int(len(csv)/no_to_return)
            # csv = combined.loc[0::no_to_skip]

            return 'combined csv file has been created'

    else:
        return {'error': 'User does not exist'}