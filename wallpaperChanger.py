#!/usr/local/bin/python3
from appscript import *
import argparse
import subprocess
import time

def wallChanger():
    i = 0
    image = ""
    error = False
    while True:
        subprocess.call("clear")
        print("Select an option:\n")
        print("  1- Set day wallpaper")
        print("  2- Set night wallpaper")
        print("  3- Set custom wallpaper")
        selection = input()
        subprocess.call("clear")
        if selection == "1":
            image = "/Users/Diego/day.png"
            break
        elif selection == "2":
            image = "/Users/Diego/night.png"
            break
        elif selection == "3":
            path = input("Enter the path to the picture: ")
            image = path.replace("'", "")
            break
        else:
            print("Please select an option from the list")

    se = app('System Events')
    desktops = se.desktops.display_name.get()
    for d in desktops:
        try:
            desk = se.desktops[its.display_name == d]
            desk.picture.set(mactypes.File(image))
        except CommandError:
            error = True
            print("The path you entered is not valid")
            print("Exiting...")
            time.sleep(2)
            subprocess.call("clear")
            break
    if not error:
        print("Your wallpaper was changed successfully")
        print("Exiting...")
        time.sleep(2)
        subprocess.call("clear")


wallChanger()
