
"""
CLIENT_KEY: 6g4fk66kr4w6bxw
CLIENT_SECRET: 2f0dlihlqgak410

get authorization_code
REQUEST 
curl https://www.dropbox.com/oauth2/authorize?client_id=6g4fk66kr4w6bxw&response_type=code&token_access_type=offline

RESPONSE
AUTHORIZATION_CODE: h6pVHtHLNWAAAAAAAAAbyT0k8aWDPe7PgXLrUMvTA-s

get refresh token
REQUEST
curl https://api.dropbox.com/oauth2/token -d code=h6pVHtHLNWAAAAAAAAAbyrwe9nSi5CnV0_YY7r1-agQ -d grant_type=authorization_code -u 6g4fk66kr4w6bxw:2f0dlihlqgak410

RESPONSE
REFRESH_TOKEN: n_CPSSng9sMAAAAAAAAAAacmxVP51kmp8hvJj19R5NilJzeCOmhZ-bgt71jbpZ3D
 
get new refresh token
REQUEST
curl https://api.dropbox.com/oauth2/token -d refresh_token=n_CPSSng9sMAAAAAAAAAAacmxVP51kmp8hvJj19R5NilJzeCOmhZ-bgt71jbpZ3D -d grant_type=refresh_token -d client_id=6g4fk66kr4w6bxw -d client_secret=2f0dlihlqgak410

https://api.dropbox.com/oauth2/token?refresh_token=FyhKD_fSCsEAAAAAAAAAARHKA2St6auV0qnOOUzdX6ZHppdb2PRMamtohDDmjd34&grant_type=refresh_token&client_id=6g4fk66kr4w6bxw&client_secret=2f0dlihlqgak410
"""

import json
import os
import webbrowser
import subprocess
import requests

appFolder = r"C:\\Users\\giova\\Documents\\loseweight"
client_id= "sr6ijak4iq3klgq"
client_secret= "cyb2kzlv6189xxu"

def openUrl(url):
  webbrowser.open(url, new=2)
  
  
def getAuthorizationCode():
  url = "https://www.dropbox.com/oauth2/authorize?client_id="+client_id+"&response_type=code&token_access_type=offline"
  openUrl(url)


def getRefreshToken(auth_code):
  url = "https://api.dropbox.com/oauth2/token"
  jsondata =  {"code": auth_code,
           "grant_type": "authorization_code",
           "client_id": client_id,
           "client_secret": client_secret
  }

  x = requests.post(url, data=jsondata)
  refreshtoken = json.loads(x.text)["refresh_token"]
  print("refresh token: " + refreshtoken)
  return refreshtoken

def getAccessToken(refresh_token):
  url = "https://api.dropbox.com/oauth2/token"
  jsondata =  {
           "grant_type": "refresh_token",
           "refresh_token": refresh_token,
           "client_id": client_id,
           "client_secret": client_secret
  }

  x = requests.post(url, data=jsondata)
  accesstoken = json.loads(x.text)['access_token']
  print("access token: " + accesstoken)
  return accesstoken

def encryptAccessToken():
  url = "http://localhost:8000/encrypt_access_token.html"
  #openUrl(url)
  #subprocess.call("cd "+appFolder+" && python serve.py", shell=True)
  
getAuthorizationCode()
auth_code = input("paste authorization code: " )
refresh_token = getRefreshToken(auth_code)
access_token = getAccessToken(refresh_token)
jsondata = {"access_token": access_token}
path = os.path.join(appFolder, "uncryptedAccessToken.json")
with open(path, "w") as writer:
  json.dump(jsondata, writer)

def updateAuto(interval):
    while True:
        print("refreshing access token")
        encryptAccessToken()  
        print("update successful")
        now = datetime.datetime.now()
        added_seconds = datetime.timedelta(0,interval)
        new_datetime = now + added_seconds
        nextUpdate = new_datetime.strftime("%A, %B %d %Y %r")
        print("next update is " + nextUpdate)
        time.sleep(interval)

#interval =  240 * 60 # minute * 60 seconds
#updateAuto(interval)