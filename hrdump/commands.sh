#!/bin/bash

function hrdump() {
    PRESENT_DIR=$(pwd)
    cd
    cd /Users/vipul/Documents/coding/python_automation/hrdump
    PRINT=`python hrdump.py $PRESENT_DIR`
    echo "$PRINT"
    cd
    cd $PRESENT_DIR
}
