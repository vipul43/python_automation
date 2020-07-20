
function create() {
    PRESENT_DIR=$(pwd)
    cd
    cd /Users/vipul/Documents/coding/python_automation/create
    CHANGE_DIR=$(python create_project.py $1)
    for i in $CHANGE_DIR
    do
        if [ $i = "SUCCESS" ]
        then
            echo "EXIT: 0"
            echo "Successfully created the git repository $1"
            echo "Successfully cloned the git repository $1"
            cd /Users/vipul/Documents/coding/github/$1
        elif [ $i = "NAME_ERR" ]
        then
            echo "NAME_ERR: No project name mentioned"
            echo "FIX: Pass a project name as an argument to command create"
            echo "DEM: \"create project_name\""
        elif [ $i = "DIR_ERR" ]
        then
            echo "DIR_ERR: $1 project already exists"
            echo "FIX: choose a different project name"
        elif [ $i = "SEL_ERR" ]
        then
            echo "SEL_ERR: Selenium is not working properly"
            echo "FIX: try after some time"
            cd $PRESENT_DIR
        fi
    done
}
