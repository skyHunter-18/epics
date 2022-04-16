import pyrebase

firebase_config = {
    "apiKey": "AIzaSyAioSEkUFKf2ZZWeXddc0wSHU9oZNX79Sk",
    "authDomain": "epicstester-31f2f.firebaseapp.com",
    "databaseURL": "https://epicstester-31f2f-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "epicstester-31f2f",
    "storageBucket": "epicstester-31f2f.appspot.com",
    "messagingSenderId": "873074115627",
    "appId": "1:873074115627:web:a658b1e5ecb442186b166e",
    "measurementId": "G-S7JJVKN340"
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

for data in db.child("user_complaint").child().get():
    address = data.val().get('address')
    date = data.val().get('date')
    mobile = data.val().get('mobile')
    name = data.val().get('name')
    pincode = data.val().get('pincode')
    status = data.val().get('status')
    img = data.val().get('image')
    print(f"img: {img}")