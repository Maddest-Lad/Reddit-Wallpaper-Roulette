import csv
import ctypes
import json
import random
import subprocess
import sys
import time
from os import path, getcwd, makedirs, chdir, system
from urllib import request, error

# Check What Platform We're In
platforms = {
    'linux1': 'Linux',
    'linux2': 'Linux',
    'darwin': 'OS X',
    'win32': 'Windows'
}

platform = platforms[sys.platform]

if sys.platform not in platforms:
    sys.exit(["Unfortunately, Your Operating System Isn't Supported"])

# Constants & Important Variables
subreddits = []

with open("subreddits.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
        # lazy way, didn't want to bother with reading csv column into list
        subreddits.append(lines[0])

save_all_images = True

# File Path
file_path = path.join(getcwd(), "image_storage")

# Create Image Storage Folder
if not path.exists(file_path):
    makedirs(file_path)

# Choose That Filepath
chdir(file_path)

# Automatically Choose
choice = random.choice(subreddits)

# Find Daily Top Post - AFAIK it's magic
url = "https://www.reddit.com/r/" + choice + "/search.json?q=url%3A.jpg+OR+url%3A.png&sort=top&restrict_sr=on&t=day"

while True:
    try:
        posts_as_json_raw_text = request.urlopen(url).read()
        break
    except error.HTTPError:
        time.sleep(5)

decoded_json = json.loads(posts_as_json_raw_text.decode('utf-8'))
top_post = decoded_json["data"]["children"][0]["data"]

# Name Image From Time, Should Avoid Any Collisions
image_filename = "bg_" + str(int(round(time.time() * 1000))) + ".jpg"
final_path = path.join(file_path, image_filename)
open(final_path, "wb").write(request.urlopen(top_post["url"]).read())

final_path = path.realpath(final_path)

# Set Background
# print(path.realpath(final_path))

if platform == "Windows":
    ctypes.windll.user32.SystemParametersInfoW(20, 0, final_path, 0)

elif platform == "OS X":

    # Mac Stuff Stolen From Here: https://github.com/vegasbrianc/mac-background/blob/master/background.py
    # Author Brian Christner

    cmd = """/usr/bin/osascript<<END
    tell application "Finder"
    set desktop picture to POSIX file "%s"
    end tell
    END"""

    subprocess.Popen(cmd % final_path, shell=True)
    subprocess.call(["killall Dock"], shell=True)

else:  # Linux

    # Linux Stuff Stolen From Here: https://github.com/geekpradd/PyWallpaper
    # Author Pradipta Bora

    def get_output(command):
        p = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        out, err = p.communicate()
        return out


    try:
        v = int(get_output("gnome-session --version").split()[-1][0])
        if v == 2:
            system("gconftool-2 --type=string --set /desktop/gnome/background/picture_filename {0}".format(final_path))
        elif v == 3:
            system('gsettings set org.gnome.desktop.background picture-uri "file://{0}"'.format(final_path))
    except error:
        raise OSError("Wallpaper Change is supported in GNOME 2/3 and Unity only")
