#!/bin/bash

function proj() {
    PRESENT_DIR=$(pwd)
    cd
    cd /Users/vipul/Documents/coding/python_automation/proj
    PRINT=`python proj.py $PRESENT_DIR`
    echo "$PRINT"
    cd
    cd $PRESENT_DIR
}
