# python_automation
- automating stuff using python
- credits:
  - created by referencing kalle hallden 
  - link to kalle halden's youtube channel: https://www.youtube.com/kallehallden
  
# Documentation

## create
- command: create reponame
- takes one argument, reponame if argument not provided raises "NAME_ERR" and aborts further procedure
- checks for folders with same name in github folder(all repos created are cloned into this folder) if found raises "DIR_ERR" and aborts further procedure
- creates new repo on github with title as reponame if failed raises "SEL_ERR"
- clones the new repo link in the folder github
- opens the new repo in vs code
- changes directory to the reponame directory
## nfe
- command: nfe filename foldername extension searchfoldername
- takes four arguments, filename of the file to open or create, creates file in the foldername after searching for the foldername in home or specified directory if mentioned as fourth optional argument with the extension as extension
- if fourth argument searchfoldername is specified then searches for the foldername in that folder, by default searched in whole home, if foldername found changes directory to that folder name else raises "DIR_ERROR" and fixes it by creating new folder with foldername in general directory
- a list of extensions is selected from the most used extensions, if any extension other than the one in the list is provided raises "EXT_ERROR" and automatically fixes it by creating the file with default extension ".txt"
- if file with filename doesnot exit in the selected folder then raises "FILE_ERROR" and fixes it by creating new file with filename and selected extension
- changes directory to the foldername directory
- opens the filename in vscode
## tit
- command: tit interpreter/compiler filename
- takes two arguments, interpreter and filename and executes "interpreter filename"
- saves time before the execution of the file using interpreter and saves time after the execution of file using interpreter
- calculates time taken for execution by calculating the difference between both saved times
- echoes the time
## cpfile
- command: cpfile filename
- takes one argument, the filename and creates that file and copies template file to that file
- navigates to current directory and creates file with name as filename
- copies the corresponding cp template file(cpp/python) depending on the extension of filename
- pastes it to the filename
- keeps the current directory same as before
## daily
- command: daily
- periodicity: 12:00AM daily
- takes no arguments
- checks for markdown file with current date if available then reports back
- if not available creates and reports back
- periodically checks for file with current date if available then goes back to sleep
- if not available creates and logs it to .daily file and then sleeps
