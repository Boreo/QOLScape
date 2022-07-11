# QOLScape
Scripts to assist regular gameplay of OldSchool RuneScape (OSRS) with minimal risk of a ban as they are designed to be run alongside human interaction.

Windows compatability only, tested working on python v3.10.5

Currently only developed autoprayflick, more to come!

# Setup
- Download and install Python - https://www.python.org/downloads/

- Download pip for Python using tutorial from - https://phoenixnap.com/kb/install-pip-windows

- Install Python libraries using Command Prompt (CMD) or Powershell:

    ```{pip install pynput pyautogui pywin32 Pillow opencv-python}```

- Run desired script using CMD or Powershell

    `python .\autoprayflick.py`
    
# Configuration
>`TODO:` This might be better as a YML for user friendliness

Set your variables in `config.py` if you wish to change certain aspects of the scripts such as random distribution etc. This is a python script itself, so formatting should remain the same.


# Auto Pray Flick
Flicks quick prayer when mouse is hovering over the prayer orb. 
## Setup
- From RuneLite's plugin-hub install `Visual Metronome`.  The location of the metronome should be visible when starting the script. Make sure `tick number` is `ticked` and `tick count` is set to `1` and tick number colour is set to `000000`.
 >Note: The colours of the metronome shouldn't matter as its using greyscale, although these are the settings I've tested.
https://user-images.githubusercontent.com/7530279/178341650-31d07e37-9ca6-4a7d-9385-105687570fe7.mp4
