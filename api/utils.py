import os 
import numpy as np 

def get_landmark(path):
    dir_path, file_name_extension = os.path.split(path)
    file_name = os.path.splitext(file_name_extension)[0] 

    file_name_components = file_name.split('_')
    landmark_string = file_name_components[-1]
    landmark_list = landmark_string.split(',')
    landmark_list_int = list(map(int, landmark_list))
    landmark = np.array(landmark_list_int)  # 1-d array

    return landmark
