# Import moduels
import os, sys, time, shutil
from pathlib import Path
from configparser import ConfigParser


#list = os.listdir(".")
#x = 0
#q = []
#while x < len(list):
#    q = [os.path.isdir(list[x])]
#    x += 1
#    print(q)
#sys.exit()


# Create config.ini file
if os.path.isfile("config.ini") == False:
    parser = ConfigParser()
    parser["CONFIG"] = {
        "path": "null",
        "setup": "1"
    }
    with open("config.ini", "w") as conf:
        parser.write(conf)
else:
    pass


# Read config values
parser = ConfigParser()
parser.read("config.ini")
config = parser["CONFIG"]
path = parser.get("CONFIG", "path")
setup = parser.get("CONFIG", "setup")


# Check if Qobuz downloader path has already been set and if not set it as a valid user input
notvalid = True
while notvalid:
    if setup == "1":
        QobuzPath = input("Enter the Qobuz donwloader path: ")
        if os.path.isdir(QobuzPath) == False:
            print("Path dosent exist, try agien")
        else:
            config["path"] = QobuzPath
            config["setup"] = "0"
            with open("config.ini", "w") as conf:
                parser.write(conf)
            notvalid=False
            path = parser.get("CONFIG", "path")
            os.chdir(path)
    elif setup == "0":
        if os.path.isdir(path) == False:
            notvalid = True
            while notvalid:
                QobuzPath = input("Qobuz path no longer exists, please enter it agien: ")
                if os.path.isdir(QobuzPath) == False:
                    print("Path dosent exist, try agien")
                else:
                    config["path"] = QobuzPath
                    config["setup"] = "0"
                    with open("config.ini", "w") as conf:
                        parser.write(conf)
                    notvalid=False
                    path = parser.get("CONFIG", "path")
                    os.chdir(path)
        else:
            QobuzPath = path
            config["path"] = QobuzPath
            config["setup"] = "0"
            with open("config.ini", "w") as conf:
                parser.write(conf)
            notvalid=False
            path = parser.get("CONFIG", "path")
            os.chdir(path)
    else:
        QobuzPath = path
        os.chdir(path)
        notvalid=False


# Set variables
f_24_96 = "FLAC (24bit-96kHz)"
f_24_44 = "FLAC (24bit-44.1kHz)"
f_16_44 = "FLAC (16bit-44.1kHz)"
mp3 = "MP3"
correctdir = None


# Get artist and album from user
notvalid = True
while notvalid:
    artist = input("Enter artist name: ")
    if os.path.isdir(artist) == False:
        print("Artist dosent exist, try agien")
    else:
        notvalid = False
        os.chdir(artist)

notvalid = True
while notvalid:
    album = input("Enter album name: ")
    if os.path.isdir(album) == False:
        print("Album dosent exist, try agien")
    else:
        notvalid = False
        os.chdir(album)


# Change directory
if os.path.exists(f_24_96):
    os.chdir(f_24_96)
    correctdir = f_24_96
elif os.path.exists(f_24_44):
    os.chdir(f_24_44)
    correctdir = f_24_44
elif os.path.exists(f_16_44):
    os.chdir(f_16_44)
    correctdir = f_16_44
elif os.path.exists(mp3):
    os.chdir(mp3)
    correctdir = mp3
else:
    print("Cannot find any music :( Exiting...")
    time.sleep(2.3)
    sys.exit()


# Delete artwork
if os.path.exists("Cover.jpg"):
    os.remove("Cover.jpg")
else: print("Cannot remove artwork as none exists, continuing")


# Remove "FORMAT (Bit depth, bitrate)" folder
os.chdir("..")
os.rename(correctdir, "placehold")
albumdir = os.getcwd() + "/placehold"
os.chdir("..")
movedir = os.getcwd() + "/placehold"
shutil.move(albumdir, movedir)
os.rmdir(album)
os.rename("placehold", album)
# I just wanted line 145 ヾ(•ω•`)o