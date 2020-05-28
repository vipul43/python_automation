
function tit() {
    PRESENT=$(date +"%s")
    $1 $2
    FUTURE=$(date +"%s")
    let TIME="$FUTURE-$PRESENT"
    echo "Executed in $TIME second"
}
