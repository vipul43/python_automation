#!/bin/bash

function nfe() {
    PRESENT_DIR=$(pwd)
    cd
    cd /Users/vipul/Documents/coding/python_automation/nfe
    python notes.py $1 $2 $3
    cd $PRESENT_DIR
}