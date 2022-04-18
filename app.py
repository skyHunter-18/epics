import pyrebase
from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from flask_login import LoginManager, login_user, logout_user, login_required

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

# initialize the login_manager
login_manager = LoginManager()

# pass your app into the login_manager instance
# login_manager.init_app(app)

# You also need to tell flask_login where it should redirect 
# someone to if they try to access a private route.
# login_manager.login_view = "login_page"

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

@app.route("/base", methods=['GET', 'POST'])
def base_page():
    return render_template("base.html")


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
@app.route("/index.html", methods=['GET', 'POST'])
def home_page():
    return render_template("index.html")


@app.route("/complaints", methods=['GET', 'POST'])
# @login_required
def public_complaint_page():
    count = 0
    for i in db.child("user_complaint").child().get():
        count += 1
    return render_template("public_complaint.html", db=db, count=count)


logged_in = None



class LoginForm(FlaskForm):
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

em = None
@app.route("/employee", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    
    if request.method == 'POST':
        email_address = request.form['email_address']
        password = request.form['password']
        global em
        em = email_address
        try:
            user = auth.sign_in_with_email_and_password(email_address, password)
            # user_id = user['idToken']
            # session['usr'] = user_id
            # au = auth.get_account_info(user_id)
            global logged_in
            logged_in = True
            return redirect(url_for('employee_complaint_page', em=em, logger=logged_in))
        except:
            flash(f'Please check your credentials and try again', category='danger')
            print("invalid")
    return render_template("login.html", form=form)

@app.route("/employee_control", methods=['GET', 'POST'])
def employee_complaint_page():
    if logged_in:
        if request.method == 'POST':
            updated_status = request.form['update_status']
            mob = request.form['mob']
            db.child("user_complaint").child(mob).update({"status": updated_status})
        if ('user' in session):
            return render_template("employee_complaint.html", db=db, s=session['user'])
        else:
            return render_template("employee_complaint.html", db=db)
    else:
        flash(f'Only Logged In Employees can access this page', category='danger')
        return redirect(url_for("login_page"))

@app.route("/logout")
def logout_page():
    # logout_user()
    global logged_in
    logged_in = None
    flash(f"You have been logged out!", category='info')
    return redirect(url_for("login_page"))