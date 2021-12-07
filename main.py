from flask import Flask, redirect, url_for

app = Flask(_name_)


@app.route('/')
def my_home():
    return "welcome to my home page"


@app.route('/homepage')
def homepage():
    return redirect(url_for('my_home'))


@app.route('/home')
def home():
    return redirect('/')


if _name_ == '_main_':
    app.run()
