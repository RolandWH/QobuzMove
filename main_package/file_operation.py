import os
import shutil
from main_package import global_vars


# Function to find out if the is a folder matching the QobuzDownloaderX format in current directory
def search_dirs():
    music_dir_names = ['FLAC (24bit-192kHz)',
                       'FLAC (24bit-96kHz)',
                       'FLAC (24bit-44.1kHz)',
                       'FLAC (16bit-44.1kHz)',
                       'MP3']

    for item in music_dir_names:
        if os.path.isdir(item):
            global_vars.bitrate_name = item
            break
        else:
            continue


def operation():
    # Remove the cover artwork if any exists
    if os.path.isfile('Cover.jpg'):
        os.remove('Cover.jpg')
    else:
        print('Cannot remove artwork as none exists, continuing')

    # Create variables for the full path of the directories to move from and to
    os.chdir('..')
    source_dir = os.getcwd() + '/' + global_vars.bitrate_name

    os.chdir('..')
    destination_dir = os.getcwd() + '/' + global_vars.bitrate_name

    shutil.move(source_dir, destination_dir)  # Do the actual moving
    os.rmdir(global_vars.album_name)  # Remove the now empty album directory
    # Rename the copied folder to the same name as the album
    os.rename(global_vars.bitrate_name, global_vars.album_name)
