Simple MP3 Player

- Written in Python 3.4.3
- using pygame 1.9.2b1




To install pygame:
from the command prompt or Terminal, run the following:

- python -m pip install --upgrade pip
- python -m pip install pygame




This player will only play .mp3 files. I set it up so that a user can select a directory from his or her computer. The app will then search for all .mp3 files in that directory, and all sub directories. It will shuffle these .mp3 files and then play them in that order until complete. It will never play an .mp3 file twice before going through the entire list, unless you hit the previous or next button. The player maintains the list after closing.




![screenshot-simple mp3 player](https://cloud.githubusercontent.com/assets/7481680/20872199/a9e0dad8-ba6a-11e6-918e-7d8ff90cb1a1.png)




TODO:

1. Error handling for problem songs/directories
