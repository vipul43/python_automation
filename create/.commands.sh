
function create() {
    PRESENT_DIR=$(pwd)
    cd
    cd /Users/vipul/Documents/coding/python_automation/create
    python create_project.py $1
    cd $PRESENT_DIR
}
