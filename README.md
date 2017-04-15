# Scripts
Just a few handy scripts.

## addExifDateToFileName/
Sorting through old photos is a pain in the ass. Most of them have a useless title, with the date the photo was taken buried in the exif data, and not available casually in finder.

This script grabs the created date from the exif and prepends it to the file name.

## arkPaths/
When I sailed the Atlantic with the Atlantic Rally for cruisers, the boats all had trackers. I was able to extract the GPS data and the list of boats from their online javascript fleet viewer.

Then I wanted to process that data into a format that would work for google earth, or other things online. I didn't have good internet to find the right way to do this, so I used google earth to save a "tracks" file in kml format, reverse engineered how that works, and wrote this python script to generate a new kml for each boat in the fleet.

The result is each boat has a file that shows its path.

## webAutomomatinScripts/
Just things that are handy for dev.

### findAwsUserByKey.py
If you've ever managed users on AWS IAM, you know finding a user from a key is a pain in the ass. This does that for you.

### saveHerokuConfig.py
Forever toying with heroku configurations. They're the only thing not in the codebase's git repo. It's nice to just archive them all every now and again.
