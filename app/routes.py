from app import app

# jsonify works the same way that JSON.stringify does
# request is what allows us to take in parameters in the api call
from flask import render_template, jsonify, request

# don't confuse with request method above, requests is a library for calling api's, it is  specific to python, where request above is specific to flask
import requests


# index is going to call weather api and show information on front
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
