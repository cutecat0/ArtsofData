#!/usr/bin/env python3
import logging
from flask import Flask
from flask import request

logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)


# @app.route('/')
def powers(n=10):
    return ','.join(str(2 ** i) for i in range(n))


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def sign():
    # read form context from request object：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run()
