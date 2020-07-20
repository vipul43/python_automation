
function cpfile() {
    PRESENT_DIR=$(pwd)
    cd
    cd /Users/vipul/Documents/coding/python_automation/cpfile
    MSG=$(python cp_file_creation.py $1 $PRESENT_DIR)
    cd
    cd $PRESENT_DIR
    if [ $MSG = "SUCCESS" ]
    then
        echo "EXIT: 0"
        echo "Successfully created cp file"
        echo "Successfully copied template file"
        echo "FINISHED"
    fi
}