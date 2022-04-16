from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import pandas as pd
import numpy as np

application = Flask(__name__)

courses = {
    "1": {
        "position": "PG (Point Guard)",
        "video": "https://www.youtube.com/watch?v=sjg1J-OimBA",
        "courtPosition": "resources/PG_position.jpg",
        "courtMoveMap": "resources/PG_movemap.jpg",
        "description": "Brain of a team. Mainly responsible for dribbling ball through the court, organizing tactic and"
                       " passing ball to teammate with space to shot. "
                       "Famous player: Magic Johnson, Stephen Curry, Chris Paul"
    }
}

# ROUTES
@application.route('/')
def homepage():
    return render_template('homepage.html')


if __name__ == '__main__':
   application.run(debug = True)
