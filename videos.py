import os, os.path
import random

# set relative path
SCRIPT_DIR = os.path.dirname(__file__)
RELATIVE_PATH = os.path.join(SCRIPT_DIR, 'jjvideos')
PATH_TO_VIDEOS = os.chdir(RELATIVE_PATH)
VIDEO_EXTENSION = ".txt"

def get_random_video():
    n_files = len([name for name in os.listdir(PATH_TO_VIDEOS) if os.path.isfile(name)])
    random_nr = random.randint(1, n_files + 1)
    str_file = str(random_nr) + VIDEO_EXTENSION
    
    return os.path.join(PATH_TO_VIDEOS, str_file)