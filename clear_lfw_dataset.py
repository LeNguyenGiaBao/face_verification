# link dataset: http://vis-www.cs.umass.edu/lfw/
import os 
import glob 
import shutil
# 5749 folders
# 13233 images

dataset_path = '../data_verify/lfw/*/'
for folder in glob.glob(dataset_path):
    file_paths = folder + '*.*' # get all file with any extension
    if len(glob.glob(file_paths)) == 1:
        shutil.rmtree(folder)

print(len(glob.glob(dataset_path)))
print(len(glob.glob(dataset_path+'*.*')))

# 1680 folders
# 9164 images