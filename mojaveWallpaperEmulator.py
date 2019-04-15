#!/usr/local/bin/python3
from appscript import *
import argparse
import time
import datetime

def setWallpaper(hour):
    se = app('System Events')
    desktops = se.desktops.display_name.get()
    for d in desktops:
        desk = se.desktops[its.display_name == d]
        desk.picture.set(mactypes.File("Wallpapers/Mojave" + str(hour) + ".jpeg"))


setWallpaper(datetime.datetime.now().hour)
print("Press CTRL + C at any time to exit.")
print(f"Changed wallpaper to {datetime.datetime.now().hour}:00 variant.")
time.sleep((60*(60-datetime.datetime.now().minute)) - datetime.datetime.now().second)
while True:
    setWallpaper(datetime.datetime.now().hour)
    print(f"Changed wallpaper to {datetime.datetime.now().hour}:00 variant.")
    time.sleep(3600)
