#!/bin/bash

while true
do
   # Get the current hour
   current_hour=$(date +"%H")

   # Check if the current hour is between 6 AM and 9 PM
   if [[ $current_hour -ge 6 && $current_hour -lt 22 ]]; then

       echo "Running hekll.py..."
       python3 hekll.py
       echo "hekll.py finished."
       sleep 2m

       echo "Running make_format_entry.py..."
       python3 make_format_entry.py
       echo "make_format_entry.py finished."
       sleep 2m

       echo "Running replace_file.py..."
       python3 replace_file.py
       echo "replace_file.py finished."
       sleep 1m

       cd ~/kodi_tv/kodi_tv_custom/
       echo "Running commit.sh..."
       bash ~/kodi_tv/kodi_tv_custom/commit.sh
       echo "commit.sh finished."
       cd ~/kodi_tv/grabber/

   else
       echo "Outside of operating hours. Current hour: $current_hour"
   fi

   # Sleep for 2 hours before the next loop iteration
   sleep 2h
done

