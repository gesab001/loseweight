#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
import json
import os
import subprocess
# Create instance of FieldStorage 

form = cgi.FieldStorage() 

# Get data from fields
access_token = form.getvalue('access_tokenInput')
jsondata = {"jesuslovesyou": access_token}



subprocess.call("py pushtogit.py")
print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
try:
  path = "access_token.json"
  with open(path, "w") as outfile:
    json.dump(jsondata, outfile)
  print ("<h2>Successfully updated access_token to  %s </h2>" % (access_token))  
except Exception as e:
  print ("<h2>error  %s </h2>" % (e))

print ("</body>")
print ("</html>")