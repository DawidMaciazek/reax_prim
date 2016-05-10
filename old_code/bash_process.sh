#!/bin/bash

outfile='out.txt'

echo "start" > $outfile

i=0
while [ $i -lt 30 ]; do
  echo $i >> $outfile
  sleep 1
  ((i++))
done
