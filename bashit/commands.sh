#!/bin/bash

function bashit() {
	touch $1
	echo "#!/bin/bash" >> $1
	chmod 744 $1 
}
