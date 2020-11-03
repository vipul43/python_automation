#!/bin/bash

function dump() {
    PRESENT_DIR=$(pwd)
    cd
    cd /Users/vipul/Documents/coding/python_automation/dump
    PRINT=`python dump.py $PRESENT_DIR $1`
    echo "$PRINT"
    cd
    cd $PRESENT_DIR
}
