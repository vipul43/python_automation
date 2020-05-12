import sys
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
sys.path.insert(1, '/Users/vipul/Documents')
from secrets import user, secret
import time


def folderAlreadyExists(title):
    #checking for the folder with same name
    #if yes return true
    #else return false
    for x in os.listdir('.'):
        if(x==title):
            return True
    return False    

    
def createRepoGithub(title):
    #selenium part
    options = Options()
    options.headless = True
    #running in headless mode
    browser = webdriver.Firefox(options=options)
    #open browser and get github site
    browser.get("https://github.com/login")
    time.sleep(1)

    #enter username
    username = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
    username.send_keys(user)
    time.sleep(1)

    #enter pass word
    password = browser.find_elements_by_xpath("//*[@id='password']")[0]
    password.send_keys(secret)
    time.sleep(1)

    #sign in account
    sign_in = browser.find_elements_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[9]")[0]
    sign_in.click()
    time.sleep(4)

    #get new repo creating page
    browser.get("https://github.com/new")
    time.sleep(1)

    #enter new repo name
    repo_name = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
    repo_name.send_keys(title)
    time.sleep(1)

    #initialize new repo with read me 
    initialize_readme = browser.find_elements_by_xpath("//*[@id='repository_auto_init']")[0]
    initialize_readme.click()
    time.sleep(1)

    #create repo
    create_repo = browser.find_elements_by_css_selector('button.first-in-line')[0]
    create_repo.submit()
    time.sleep(8)

    # quit browser
    browser.quit()


def createProject():
    try:
        # get argument
        title = sys.argv[1]
    except Exception:
        # if argument doesnot exist raise error
        print("NAME_ERR")
    else:
        os.chdir("/Users/vipul/Documents/coding/projects")
        # checking for folder with same name
        # if no proceeding to create new folder and git repo
        if(not folderAlreadyExists(title)):
            #create repo
            createRepoGithub(title)
            #create directory
            clone_link = "https://github.com/vipul43/" + title + ".git"
            os.system("git clone " + clone_link)
            os.system("code " + title)
            os.system("cd ./" + title)
            #exit with success message
            #checking for this success message in shell script
            #VERY IMP PRINT STATEMENT
            print("SUCCESS")
        else:
            # else raise error
            print("DIR_ERR")

if __name__ == "__main__":
    createProject()