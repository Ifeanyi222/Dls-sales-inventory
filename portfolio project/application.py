from flask import Flask, render_template, request, url_for, flash, session
import hashlib
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'linusifykey' # set a secret key for session
users = {'user1': 'password'} # dictionary for username and password
app.config['SQLALCHEMY_DATABASE_URL']='mysql://linusify:Akuify2018#@localhost/dls_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50), unique=True)
    


@app.route("/")
def landing():
    return render_template("landingpage.html")

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")



@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")
        




if __name__ == "__main__":
    app.run(debug=True)
