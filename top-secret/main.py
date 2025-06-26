from flask import Flask, render_template ,request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField("Log in")


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login",methods = ["GET","POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    if request.method == 'GET':
        return render_template('login.html', form=login_form)
    if login_form.email.data == "admin@gmail.com" and login_form.password.data == "12345678":
        return render_template("success.html")
    else:
        return render_template("denied.html")


        


if __name__ == '__main__':
    app.run(debug=True)