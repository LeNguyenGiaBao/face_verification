import numpy as np 
import os 

def get_landmark(list_string):
    list_int = list(map(int, list_string))
    landmark_array = np.array(list_int)
    landmark = landmark_array.reshape((5, 2))
    
    return landmark

def process_path(path):
    dir_path, file_name_extension = os.path.split(path)
    file_name = os.path.splitext(file_name_extension)[0] 

    file_name_components = file_name.split('_')

    mask = int(file_name_components[-2])
    landmark_string = file_name_components[-1]
    landmark_list = landmark_string.split(',')
    landmark = get_landmark(landmark_list)

    return landmark