import ctypes
import json
import random
import time
from os import path, getcwd, makedirs, chdir
from urllib import request, error

# Constants & Important Variables
names = ["happy", "standard", "funny"]
happy_subreddits = ["aww", "WhatsWrongWithYourDog"]
standard_subreddits = ["pics", "Images", "wallpaper", "itookapicture", "Art", "generativeart", "generative",
                       "CozyPlaces"]
funny_subreddits = ["Beans", "delusionalartists", "classicalartmemes"]
combined = (happy_subreddits, standard_subreddits, funny_subreddits)

timeout = 10  # Time Out time for the user selection
choice = None  # which subreddit it gets an image from

user_choice = False

# File Path
file_path = path.join(getcwd(), "image_storage")

# Create Image Storage Folder
if not path.exists(file_path):
    makedirs(file_path)

# Choose That Filepath
chdir(file_path)

# Allow User To Choose Subreddit Pool, If UserChoice is False Defaults to Random Subreddit
if user_choice:

    # Fancy Way Of Printing Out Categories, h : 0-3, i : category, j : what's in each category
    for h, i, j in zip([i for i in range(0, len(combined))], names, combined):
        print(h, i, ": ", [i for i in j])

    answer = int(input("\nYou Have 10 Seconds, Please Select Your Category, Otherwise Pray to RNGesus: "))

    choice = random.choice(combined[answer])

else:
    # Chooses Randomly
    choice = random.choice(combined)

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

path.realpath(final_path)

# Set Background
print(path.realpath(final_path))
ctypes.windll.user32.SystemParametersInfoW(20, 0, path.realpath(final_path), 0)
