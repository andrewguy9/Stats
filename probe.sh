#!/bin/bash


for url in $@
do
  wget -O /dev/null -q $url
  if [ $? -eq 0 ]
  then
    echo "Success $url"
  else
    echo "Failure $url"
  fi
done

exit 0
