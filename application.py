from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from matplotlib.font_manager import json_dump
import pandas as pd
import numpy as np
import json

application = Flask(__name__)

courses = {
    "1": {
        "position": "PG (Point Guard)",
        "video": "https://www.youtube.com/embed/izzHABI1F2I?start=3",
        "courtPosition": "https://i.ibb.co/pW6TPts/PG-position.jpg",
        "courtMoveMap": "https://i.ibb.co/mFp1SMB/PG-movemap.jpg",
        "description": "Brain of a team. Mainly responsible for dribbling ball through the court, organizing tactic and"
                       " passing ball to teammate with space to shot. "
                       "Famous player: Magic Johnson, Stephen Curry, Chris Paul"
    },
    "2": {
        "position": "SG (Score Guard)",
        "video": "https://www.youtube.com/embed/wb_qC3ZcCyw",
        "courtPosition": "https://i.ibb.co/n8bv1Dt/SG-position.jpg",
        "courtMoveMap": "https://i.ibb.co/S752SnB/SG-movemap.jpg",
        "description": "Outside scorer of a team. Mainly responsible for running through half court and finding a space "
                       "to catch the ball and shot."
                       "Famous Player: Michael Jordan, Kobe Bryant"
    },
    "3": {
        "position": "SF (Small Forward)",
        "video": "https://www.youtube.com/embed/uBgtirMRQFQ",
        "courtPosition": "https://i.ibb.co/pdpLj3T/SF-position.jpg",
        "courtMoveMap": "https://i.ibb.co/H75L9cB/SF-movemap.jpg",
        "description": "Score core of a team. Mainly responsible for multiple tasks including both inside and outside "
                       "offense/defense and sometimes rebound."
                       "Famous Player: Lebron James, Larry Bird, Kevin Durant"
    },
    "4": {
        "position": "PF (Power Forward)",
        "video": "https://www.youtube.com/embed/0tbWhV-PkIY",
        "courtPosition": "https://i.ibb.co/CJXZMnH/PF-position.jpg",
        "courtMoveMap": "https://i.ibb.co/SJcn5hD/PF-movemap.jpg",
        "description": "Inside defender of a team. Mainly responsible for scrambling rebound, picking and rolling "
                       "for PG, blocking opponent in paint area and other “dirty” and tiring work. "
                       "Famous player: Tim Duncan, Kevin Garnett"
    },
    "5": {
        "position": "C (Center)",
        "video": "https://www.youtube.com/embed/j_Chf5qBQPY?start=6",
        "courtPosition": "https://i.ibb.co/x2w0Jm9/C-position.jpg",
        "courtMoveMap": "https://i.ibb.co/pymk5tG/C-movemap.jpg",
        "description": "Inside core of a team. Mainly responsible for paint area offense, scrambling rebound and "
                       "defending insider opponent. "
                       "Famous player: Dwight Howard, Shaq O’Neal"
    },
    "6": {
        "video": "https://www.youtube.com/embed/1xu8W10vymo",
        "courtImg": "https://i.ibb.co/S5n8dFX/teamposition.jpg",
        "description": "In a game, normally in both offense and defense: PG dribbles through back court, stands on top"
                       " of arc and manage tactic. SG continue running around the half court, as long as he get rid of"
                       " defender, he can catch ball and shoot outside. SF stand between inside and outside so that "
                       "he can choose flexible offense and defense transition. PF competes with opponents around paint "
                       "area and wait for rebound or give a block. C stands under the basket and posts up after "
                       "obtaining good position."
    }
}

# ROUTES


@application.route('/')
def homepage():
    return render_template('homepage.html')


@application.route("/learn/<id>")
def learn(id):
    return render_template("learn.html",  id=id)


@application.route('/getdata', methods=['GET'])
def getdata():
    id = json.loads(list(request.args.to_dict().keys())[0])['id']
    return jsonify(data=courses[str(id)])


if __name__ == '__main__':
    application.run(debug=True)
