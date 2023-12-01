#!/bin/bash

while true
do
   echo "Running hekll.py..."
   python3 hekll.py
   echo "hekll.py finished."
   sleep 2m

   echo "Running make_format_entry.py..."
   python3 make_format_entry.py
   echo "make_format_entry.py finished."
   sleep 2m

   echo "Running main_2h.sh..."
   python3 replace_file.py
   echo "main_2h.sh finished."
   sleep 2h
done

