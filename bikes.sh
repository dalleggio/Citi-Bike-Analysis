#!/bin/bash

url="http://witestlab.poly.edu/bikes/"
year=2016
months=$(seq -f "%02g" 9)
suffix="-citibike-tripdata"

# rm stations_raw.txt

for mon in $months; do
  filename="$year""$mon""$suffix"
  if [ ! -e "$filename"".zip" ]
  then
     wget "$url""$filename"".zip"
  fi
  if [ ! -e "$filename"".csv" ]
  then
     unzip $filename".zip"
  fi
done

