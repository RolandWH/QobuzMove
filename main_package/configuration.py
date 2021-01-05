import os
from getpass import getuser
from main_package import global_vars


# Set the config directory based on username
def set_config_dir():
    global_vars.config_dir = 'C:/Users/' + getuser() + '/AppData/Roaming/qobuzmv'


# Function to update which takes in a message string
# This can either be used to create the config file for the first time or to update it if it becomes invalid
def update_path(msg):
    music_path = input(msg)  # Get the music path from the user
    # Loop until a valid path is entered
    while not os.path.isdir(music_path):
        music_path = input('Sorry but that is not a valid path, please try again: ')
    # Open the config file and write the path to it
    with open('config.ini', 'w') as config_file:
        config_file.write(music_path)


# Function to read the config file by opening it and setting a global variable to the read output of the file
def read_config():
    with open('config.ini', 'r') as config_file:
        global_vars.config_data = config_file.read()
