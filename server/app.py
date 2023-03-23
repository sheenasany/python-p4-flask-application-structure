#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# define a route using the decorator
#decorators are functions that take functions as args & return
#them decorated with new features
@app.route('/') #this will represent the index route
def index():
    return '<h1>Welcome one and all!</h1>'

@app.route('/<username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)