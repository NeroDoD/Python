#!/usr/local/bin/python3
import sys
if sys.platform == "darwin": from appscript import *
from pathlib import Path
import argparse
import time
import datetime
import subprocess
import os
import wallpaperSettings

'''
There must be two folders called 'Desert' and 'Solar'
in the same path as the 'mojaveWallpaperEmulator.py' file itself.
These folders must contain 24 images named '0.jpeg', '1.jpeg'...'23.jpeg'
'''

#Gets input from the user on launch (UNUSED)
def getInput():
        while True:
                subprocess.call("clear")
                print("What wallpaper do you want to use?\n")
                print("     1- Mojave Desert")
                print("     2- Solar Gradient\n")
                choice = input()
                if choice == "1": return "Desert"
                elif choice == "2": return "Solar"
                else: print("Please enter a valid option.\nRetrying..."); time.sleep(2); subprocess.call("clear")

#macOS wallpaper 'setter'
def macOS_setWallpaper(hour):
        se = app('System Events')
        desktops = se.desktops.display_name.get()
        user = str(Path.home())[7:]
        os.chdir("/")
        for d in desktops:
                desk = se.desktops[its.display_name == d]
                desk.picture.set(mactypes.File(f"Users/{user}/.wallchanger/{folder}/{str(hour)}.jpeg"))

#Linux wallpaper 'setter'
def linux_setWallpaper(hour):
        os.system(f"gsettings set org.gnome.desktop.background picture-uri file://'{str(Path.home())}/.wallchanger/{folder}/{str(hour)}.jpeg'")

#Terminate program if it has been disabled in settings
if wallpaperSettings.programDisabled: sys.exit()

#Actual program
#folder = getInput()
folder = wallpaperSettings.folder
subprocess.call("clear")
if sys.platform == "darwin": macOS_setWallpaper(datetime.datetime.now().hour)
elif sys.platform == "linux": linux_setWallpaper(datetime.datetime.now().hour)
else:
        print("Your system is not supported.\nPress CTRL + C to exit...")
        while True: pass      
print("Press CTRL + C at any time to exit.")
print(f"Changed wallpaper to {folder} {datetime.datetime.now().hour}:00 variant.")
time.sleep((60*(60-datetime.datetime.now().minute)) - datetime.datetime.now().second)
while True:
        if sys.platform == "darwin": macOS_setWallpaper(datetime.datetime.now().hour)
        elif sys.platform == "linux": linux_setWallpaper(datetime.datetime.now().hour)
        print(f"Changed wallpaper to {datetime.datetime.now().hour}:00 variant.")
        time.sleep(3600)