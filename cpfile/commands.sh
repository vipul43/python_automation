
function cpfile() {
    PRESENT_DIR=$(pwd)
    cd
    cd /Users/vipul/Documents/coding/python_automation/cpfile
    python cp_file_creation.py $1 $PRESENT_DIR
    cd
    cd $PRESENT_DIR
}