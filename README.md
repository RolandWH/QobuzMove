# QobuzMove
Simple Python script to organize downloads created by QobuzDownloaderX into a simpler folder structure!

# Application Goals
1. Create an easy way to select album and artist from console ✔
   1. Only list folders in current directory (not files)
   1. Find a way to let the user use arrow keys to select between all the folders in the current directory
1. Remove album artwork and audio quality folder ✔
1. Check all user input to make sure it's valid ✔
   1. Check path to music is valid
1. Add errors for all scenarios where the application can't continue ✔
   1. If no audio quality folder can be found
1. Add warnings for all scenarios where the application can continue but skips certain function. :heavy_check_mark:
   1. If artwork doesn't exist
1. Create main menu so multiple operations can be performed :x:
1. Auto detect where QobuzDownloader path is :x:
1. Add options to either only remove album art or only remove audio quality folder :x:

# How the goals have been achieved
## 1 (i).
```python
def getdirs():
    q = os.listdir(".")
    global z
    z = []
    for i in q:
        if os.path.isfile(i) == False:
            z.insert(0, i)
        else:
            continue
```
The getdirs function uses the `q` variable to list all files and folders in the current directory.
It then create an empty list named `z`.
Every item in the current directory is checked to see if it is a file or not (must be a folder if not a file).
If the item being checked is a folder and not a file it is added to the `z` list.
If the item being checked is a file and not a folder it is ignored.

The result of all of this is that if we print q `>>> print(q)` we get:
- folder0
- folder1
- file0
- file1

However if print our newly created z list `>>> print(z)` we get:
- folder0
- folder1

This successfully only gets folders in the current directory and not files!

## 1 (ii).
`import questionary`
For this I used the [Questionary](https://pypi.org/project/questionary/) plugin.

```python
getdirs()
artist = questionary.select("Choose an artist: ", choices=z).ask(input)
os.chdir(artist)
```
When it is time for the user to select which artists and albums should be organized the getdirs() function created earlier is called.
I then used the `select` function in questionary. This will ask the user to select a folder from our `z` list. Once a selection is made it will be returned into the `artist` variable. The script will then change into the directory specified in the `artist` variable. This is repeated for the album.

![Questionary](https://i.imgur.com/IL3yqwC.gif)

## 2, 4(i), 5(i).
```python
if os.path.exists(f_24_96):
    correctdir = f_24_96
elif os.path.exists(f_24_44):
    correctdir = f_24_44
elif os.path.exists(f_16_44):
    correctdir = f_16_44
elif os.path.exists(mp3):
    correctdir = mp3
else:
    print("Cannot find any music :( Exiting...")
    time.sleep(2.3)
    sys.exit()
```
Once the user has selected their desired album directory it checks to see whether [these](https://i.imgur.com/EkcsWOQ.png) names exists in the folder. Once it finds one of them it marks it using the `correctdir` variable. If none of these folders are found (this means that the tool has already been run or that the folder specified does not actually contain music from QobuzDownloaderX) it will exit after printing "Cannot find any music :( Exiting..." for 2.3 seconds. [4(i)](https://github.com/RolandWH/QobuzMove/blob/master/README.md#:~:text=If%20no%20audio%20quality%20folder%20can%20be%20found).

```python
os.chdir(correctdir)
if os.path.exists("Cover.jpg"):
    os.remove("Cover.jpg")
else: print("Cannot remove artwork as none exists, continuing")
```
The script changes directory into the `correctdir` folder marked earlier. It then checks to see if the Cover.jpg (album art) file exists. If the file does exists it gets deleted, if it does not exist a warning is printed ("Cannot remove artwork as none exists, continuing") and then the application continues [5(i)](https://github.com/RolandWH/QobuzMove/blob/master/README.md#:~:text=If%20artwork%20dosen't%20exist).

```python
os.chdir("..")
albumdir = os.getcwd() + "/" + correctdir
os.chdir("..")
movedir = os.getcwd() + "/" + correctdir
shutil.move(albumdir, movedir)
os.rmdir(album)
os.rename(correctdir, album)
```
Once the album artwork has been deleted the application moves back into the album directory.
The `albumdir` variable is then assigned to the current directory + the name of the correct audio quality directory e.g.`C:/Users/Roland/Music/Qobuz/TheFatRat/Stronger/FLAC (16bit-44.1kHz)`

The script moves up one more time into the artist directory.
The `movedir` variable is then assigned to the current directory + the name of the correct audio quality directory name
e.g. `C:/Users/Roland/Music/Qobuz/TheFatRat/FLAC (16bit-44.1kHz)`

Now `albumdir` is moved to `movedir` and the original album folder is deleted because it is now empty.
The audio quality folder is the renamed to the original name of the album selected using questionary.
