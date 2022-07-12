# QOLScape
Scripts to assist regular gameplay of OldSchool RuneScape (OSRS) with minimal risk of a ban as they are designed to be run alongside human interaction.

Windows compatability only, tested working on python v3.10.5

Currently only developed autoprayflick, item dropper, never log & more coming soon!

## Setup

- Download and install Python - https://www.python.org/downloads/

- Download pip for Python using tutorial from - https://phoenixnap.com/kb/install-pip-windows

- Install Python libraries using Command Prompt (CMD) or Powershell:

    ```pip install pynput pyautogui pywin32 Pillow opencv-python colorama```

- Run desired script using CMD or Powershell

    `python .\autoprayflick.py`

- Alternatively, install PyCharm or VSC with python plugins, plenty of guides on the internet to set these up.

## Configuration

Set your variables and hotkeys in `config.py` if you wish to change certain aspects of the scripts such as random distribution etc. This is a python script itself, so formatting should remain the same.

Make sure you save this before running any script!


## Auto Pray Flick

https://user-images.githubusercontent.com/7530279/178342764-22d9a30b-bdc8-4e22-a4c5-83109dccc47d.mp4

Flicks quick prayer when mouse is hovering over the prayer orb. 

### Setup

From RuneLite's plugin-hub install **Visual Metronome**  The location of the metronome should be visible when starting the script. Make sure ***tick number*** is set `ticked` and ***tick count*** is set to `1` and tick number colour is set to `000000`.
 >Note: The colours of the metronome shouldn't matter as its using greyscale, although these are the settings I've tested.

 ![image](https://user-images.githubusercontent.com/7530279/178334449-b69fd3c5-b180-4c03-9879-d779bc8d7562.png)

### Use

- Run the script from CMD or Powershell

    `python .\autoprayflick.py`

- Disable/Enable the script with the hotkey (Default = `F1`) and exit using the hotkey (Default = `ctr+alt+c`)

- Hover mouse over prayer orb! The script will pause when mouse is outside the orb, and flick when inside. It will also check if prayer is enabled on its first click, and if disabled, enables prayer.

