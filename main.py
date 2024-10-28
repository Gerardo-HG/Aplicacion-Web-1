import os
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import Email, DataRequired, InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap5(app)

class RegisterForm(FlaskForm):
    name = StringField(label="Name",validators=[DataRequired()])
    email = EmailField(label="Email",validators=[DataRequired()])
    password = PasswordField(label="Password",validators=[DataRequired()])
    submit = SubmitField(label="Create new account")

class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Login")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/register")
def register():
    register_form = RegisterForm()

    return  render_template('register.html',form=register_form)

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


if __name__ == "__main__":
    app.run(debug=False)