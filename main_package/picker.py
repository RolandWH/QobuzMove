import os
import sys
import time
import questionary
from main_package import global_vars


# Function to find only folders in the current directory and not files
def get_dirs():
    cwd_items = os.listdir('.')
    dir_list = []
    for item in cwd_items:
        if not os.path.isfile(item):
            dir_list.append(item)
        else:
            continue
    if len(dir_list) == 0:
        print('This directory is empty!')
        time.sleep(5)
        sys.exit(0)
    return dir_list


# Function to use questionary so the user can pick artist and album through an interactive prompt
def pick_directory():
    artist = questionary.select('Choose an artist: ', choices=get_dirs()).ask()
    os.chdir(artist)
    global_vars.artist_name = artist

    album = questionary.select('Choose an album: ', choices=get_dirs()).ask()
    os.chdir(album)
    global_vars.album_name = album
