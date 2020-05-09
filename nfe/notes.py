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

java = ".java"
dart = ".dart"

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
    "dart": dart, "flutter": dart, ".dart": dart
}


"""
    nfe ==> note folder extension
    - note ==> name of the file you want to open or create
    - folder ==> name of the folder in which you want to create or open a file if exists otherwise create the folder and open or create the file
    - extension ==> name of the extension in which you want to open the file(default is set to '.txt') also the extensions are according to my workflow

"""

def create():
    extension = str(sys.argv[3])
    foldername = str(sys.argv[2])
    filename = str(sys.argv[1])
    os.chdir("./Notes")

    #confirming the extension of the file
    try:
        extension = extensions[extension]
    except Exception:
        print("EXT_ERROR: '{}' extension does not exist".format(extension))
        print("FIX: opening file with default extension '.txt'")
        extension='.txt'
    filename+=extension

    #confirming the directory of the file
    if(os.path.isdir("./" + foldername)):
        os.chdir("./" + foldername)
    else:
        print("DIR_ERROR: '{}' directory does not exist".format(foldername))
        print("FIX: creating '{}' directory".format(foldername))
        os.mkdir(foldername)
        os.chdir("./" + foldername)

    #confirming the file
    if(not os.path.isfile("./" + filename)):
        print("FILE_ERROR: '{}' file does not exist".format(filename))
        print("FIX: creating '{}' file".format(filename))
        open(filename, "a").close()
    
    os.system("code " + filename)

if __name__ == "__main__":
    create()