import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "myvideoapp-84db9.firebaseapp.com",
  "databaseURL": "https://myvideoapp-84db9.firebaseio.com/",
  "storageBucket": "myvideoapp-84db9.appspot.com",
  "serviceAccount": "auth.json"
}

firebase = pyrebase.initialize_app(config)

def getDataBase():
	return firebase.database()