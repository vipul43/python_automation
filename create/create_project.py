import sys
import os
from selenium import webdriver
from secrets import secret

def folderAlreadyExists(title):
    for x in os.listdir('.'):
        if(x==title):
            return True
    return False    
title ="newproject"
browser = webdriver.Firefox()
browser.get("https://github.com/login")

username = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
username.send_keys("vipul43")
password = browser.find_elements_by_xpath("//*[@id='password']")[0]
password.send_keys(secret)
sign_in = browser.find_elements_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[9]")[0]
sign_in.click()
browser.get("https://github.com/new")
repo_name = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
repo_name.send_keys(title)
initialize_readme = browser.find_elements_by_xpath("//*[@id='repository_auto_init']")[0]
initialize_readme.click()
create_repo = browser.find_elements_by_css_selector('button.first-in-line')[0]
create_repo.submit()
# clone = browser.find_elements_by_css_selector('span.dropdown-caret:nth-child(1)')
# clone.click()
# clone_link = browser.find_elements_by_xpath("/html/body/div[4]/div/main/div[3]/div/div[3]/span/get-repo-controller/details/div/div/div[1]/div[1]/div/input")[0]
# print(clone_link)






def createProject():
    try:
        title = sys.argv[1]
        os.chdir("/Users/vipul/Documents/coding/projects")
        if(not folderAlreadyExists(title)):
            path = "./" + title
            # os.chdir(path)
            clone_link = createRepoGithub(title)
            os.system("git clone " + clone_link)
            os.chdir("./" + title)
        else:
            print("DIR_ERR: {} project already exists".format(title))
            print("FIX: choose a different project name")
    except Exception:
        print("NAME_ERR: No project name mentioned")
        print("FIX: Pass a project name as an argument to command create")
        print("DEM: \"create project_name\"")







if __name__ == "__main__":
    createProject()