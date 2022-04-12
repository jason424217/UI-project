from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import pandas as pd
import numpy as np

application = Flask(__name__)

# ROUTES
@application.route('/')
def homepage():
    return render_template('homepage.html')


if __name__ == '__main__':
   application.run(debug = True)
