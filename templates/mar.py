import pyrebase

firebase_config = {
    "apiKey": "AIzaSyD-hX6eHS9juPxc0bWLmX-icUk4s19eE7g",
    "authDomain": "nagarseva1.firebaseapp.com",
    "databaseURL": "https://nagarseva1-default-rtdb.firebaseio.com",
    "projectId": "nagarseva1",
    "storageBucket": "nagarseva1.appspot.com",
    "messagingSenderId": "711684542132",
    "appId": "1:711684542132:web:47221a9f5c535c9c2f11e1",
    "measurementId": "G-PVV8WMHJ0X"
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()
auth = firebase.auth()

# for data in db.child("user_complaint").child().get():
#     address = data.val().get('address')
#     date = data.val().get('date')
#     mobile = data.val().get('mobile')
#     name = data.val().get('name')
#     pincode = data.val().get('pincode')
#     status = data.val().get('status')
#     img = data.val().get('image')
#     print(f"img: {img}")

user = auth.get_account_info
print(user)