import os
import sys
import time
from main_package import global_vars, configuration, picker, file_operation


# Configuration
configuration.set_config_dir()  # Set the config directory based on username
if not os.path.isdir(global_vars.config_dir):
    os.mkdir(global_vars.config_dir)  # If the config directory doesn't exist, create it
os.chdir(global_vars.config_dir)

if not os.path.isfile('config.ini'):
    # If the config.ini file doesn't exist create it using the `update_path()` function
    configuration.update_path('Please enter the path to QobuzDownloadX music folder: ')
else:
    # If the config.init file does exist then check that the path inside of it is still valid and update if not.
    configuration.read_config()
    if not os.path.isdir(global_vars.config_data):
        configuration.update_path('Sorry but the path you entered earlier no longer exists, please enter it again: ')


# Picker
configuration.read_config()  # Read the configuration file
os.chdir(global_vars.config_data)  # Change directory to the path stored in the configuration file
picker.pick_directory()  # Call the `pick_directory()` function so the user can choose artist and album


# File Operation
file_operation.search_dirs()  # Find out if the is a folder matching the QobuzDownloaderX format in the directory
if global_vars.bitrate_name != '':
    os.chdir(global_vars.bitrate_name)  # If there is then change directory into it
    file_operation.operation()  # Call the `operation()` function to do the actual reorganization of files
else:
    print("No music could be found in the directory :( Exiting...")  # If no folder is found exit with an error message
    time.sleep(2.7)
    sys.exit(0)
