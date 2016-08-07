import pyrebase

config = {
  "apiKey": "AIzaSyA1w1JSSGvTh9zMtnUf1ep6Qh0b8YUQkRM",
  "authDomain": "myvideoapp-84db9.firebaseapp.com",
  "databaseURL": "https://myvideoapp-84db9.firebaseio.com/",
  "storageBucket": "myvideoapp-84db9.appspot.com",
  "serviceAccount": "auth.json"
}

firebase = pyrebase.initialize_app(config)

def getDataBase():
	return firebase.database()