import pyrebase
from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from flask_login import login_user, logout_user, login_required

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

# data = db.child("user_complaint").child()


app = Flask(__name__)
app.config['SECRET_KEY'] = '6fb5fa23ddb7923fa814cabf'

@app.route("/base", methods=['GET', 'POST'])
def base_page():
    return render_template("base.html")


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
@app.route("/index.html", methods=['GET', 'POST'])
def home_page():
    return render_template("index.html")


# @login_required
@app.route("/complaints", methods=['GET', 'POST'])
def public_complaint_page():
    count = 0
    for i in db.child("user_complaint").child().get():
        count += 1
    return render_template("public_complaint.html", db=db, count=count)


@app.route("/employee_control", methods=['GET', 'POST'])
def employee_complaint_page():
    return render_template("employee_complaint.html", db=db)





class LoginForm(FlaskForm):
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


@app.route("/employee", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if request.method == 'POST':
        email_address = request.form['email_address']
        password = request.form['password']
        
        try:
            auth.sign_in_with_email_and_password(email_address, password)
            return redirect(url_for('employee_complaint_page'))
        except:
            flash(f'Please check your credentials and try again', category='danger')
            print("invalid")
    return render_template("login.html", form=form)