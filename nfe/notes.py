import sys
import os


#adding file extensions
text = ".txt"
markdown = ".md"
python = ".py"
c = ".c"
cpp = ".cpp"
matlab = ".m"
shell = ".sh"
javascript = ".js"
typescript = ".ts"
html = ".html"
css = ".css"
json = ".json"

java = ".java"
dart = ".dart"
ruby = ".rb"
php = ".php"
csharp = ".cs"
yaml = ".yaml"
xml = ".xml"
org = ".org"

#keywords for extensions
extensions = {
    "text": text, "txt": text, ".txt": text,
    "markdown": markdown, "mark": markdown, ".md": markdown,
    "python": python, "py": python, ".py": python,
    "c": c, "C": c, ".c": c,
    "c++": cpp, "cpp": cpp, ".cpp": cpp,
    "matlab": matlab, ".m": matlab,
    "shell": shell, "sh": shell, ".sh": shell,
    "javascript": javascript, "js": javascript, ".js": javascript, "typescript": typescript, "ts": typescript, ".ts": typescript,
    "HTML": html, "html": html, ".html": html,
    "CSS": css, "css": css, ".css": css,
    "java": java, ".java": java,
    "dart": dart, "flutter": dart, ".dart": dart,
    "yaml" : yaml, ".yaml" : yaml,
    "json" : json, ".json" : json,
    "org" : org, ".org" : org,
    "php" : php, ".php" : php,
    "ruby" : ruby, ".rb" : ruby,
    "xml" : xml, ".xml" : xml
}


"""
    nfe ==> note folder extension
    - note ==> name of the file you want to open or create
    - folder ==> name of the folder in which you want to create or open a file if exists otherwise create the folder and open or create the file
    - extension ==> name of the extension in which you want to open the file(default is set to '.txt') also the extensions are according to my workflow

"""
def findFolder(foldername):   
    path = ""
    flag = False
    #finding for the directory named foldername in Documents directory
    #os.walk returs tuples of the format (path, directories in the path, files in the path)
    #iterating through each tuple and finding the foldername directory
    #if found return True and path
    #else return False and ''

    for item in os.walk("/Users/vipul/Documents"):
        for ele in item[1]:
            if(ele==foldername):
                path=item[0] + "/" + foldername
                flag = True
                break
        if(flag):
            break
    return flag, path


def create():
    extension = str(sys.argv[3])
    foldername = str(sys.argv[2])
    filename = str(sys.argv[1])

    #confirming the extension of the file
    try:
        extension = extensions[extension]
    except Exception:
        print("EXT_ERROR: '{}' extension does not exist".format(extension))
        print("FIX: opening file with default extension '.txt'")
        extension='.txt'
    filename+=extension

    #confirming the directory of the file
    #search for a folder in whole documents directory
    #and navigate to it if found
    #else keeo the file in "/Users/vipul/Documents/general" directory
    folder_found, path = findFolder(foldername)
    if(folder_found):
        os.chdir(path)
    else:
        print("DIR_ERROR: '{}' directory does not exist".format(foldername))
        print("FIX: creating '{}' directory".format(foldername))
        os.chdir("/Users/vipul/Documents/general")
        # os.mkdir(foldername)
        # os.chdir("./" + foldername)

    #confirming the file
    if(not os.path.isfile("./" + filename)):
        print("FILE_ERROR: '{}' file does not exist".format(filename))
        print("FIX: creating '{}' file".format(filename))
        open(filename, "a").close()
    
    os.system("code " + filename)

if __name__ == "__main__":
    create()