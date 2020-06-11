# Reddit-Wallpaper-Roulette
A simple python script to set your wallpaper to the top image of the day from a random subreddit inside `subreddits.csv`.

# Windows Setup


# OSX and Linux Setup [(Based On This)](https://medium.com/@gavinwiener/how-to-schedule-a-python-script-cron-job-dea6cbf69f4e)

Warning, I Don't Have a Mac / Linux Device To Test This, It May Take Some Debugging

Run:
`crontab -e`

`0 12 * * * /usr/bin/python3 /path_to_automated_version.py >> ~/cron.log 2>&1`
