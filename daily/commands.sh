#!/bin/bash

function daily() {
    PRESENT_DIR=$(pwd)
    if [ "$PRESENT_DIR" = "/Users/vipul/Documents/todolist" ]
    then
        cd
        cd /Users/vipul/Documents/coding/python_automation/daily
        python daily_file_creation.py $PRESENT_DIR
        cd
        cd $PRESENT_DIR
    else
        echo "LOC_ERR: YOU ARE NOT IN CORRECT LOCATION"
        echo "FIX: CHANGE LOCATION TO /Users/vipul/Documents/todolist"
    fi
}

while true
do
    DATE=`date | cut -d' ' -f4`
    if [[ $DATE == "00:00:00" ]]
    then
            daily
            sleep 3600s
    fi
done
