import sys
import os

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

def create():
    extension = str(sys.argv[3])
    try:
        extension = extensions[extension]
    except Exception:
        print(extension)
        extension='.txt'

        
    print(sys.argv)
    filename = str(sys.argv[1]) + str(sys.argv[3])
    open(filename, "a").close()
    os.system("code " + filename)

if __name__ == "__main__":
    create()