import subprocess

command = "python3 -m http.server --cgi"

subprocess.call(command, shell=True)