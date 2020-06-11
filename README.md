# Reddit-Wallpaper-Roulette
A simple python script to set your wallpaper to the top image of the day from a random subreddit inside `subreddits.csv`.

# Windows Setup [(Based On This)](https://datatofish.com/python-script-windows-scheduler/)
Modify `example_windows.bat` replacing `C:\Path\To\python.exe` with the path to your python 3 executable
Then replace `C:/Path/To/automated_version.py` with your path to `automated_version.py`

Open up Windows Task Scheduler with `win r` and then entering `%windir%\system32\taskschd.msc /s`. Or you can find it somewhere in control panel.

Click Create Basic Task

Give The Task Some Random Name, Then Follow The Dialogue Until You Reach `Action` 

In `Action`, Navigate To Your `example_windows.bat` file, select it and you should be all set!

If the script keeps opening a CMD window, you may need to rename `automated_version.py` to `automated_version.pyw` and change `example_windows.bat` to reflect that. 


# OSX and Linux Setup [(Based On This)](https://medium.com/@gavinwiener/how-to-schedule-a-python-script-cron-job-dea6cbf69f4e)

Warning, I Don't Have a Mac / Linux Device To Test This, It May Take Some Debugging

Run:
`crontab -e`

`0 12 * * * /usr/bin/python3 /path_to_automated_version.py >> ~/cron.log 2>&1`
