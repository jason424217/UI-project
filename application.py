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
                       " passing ball to teammate with space to shot. In the video, look at No 3 player Chirs Paul "
                       "dribbling ball from back-court to front court and throwing ball to teammate. <br>"
                       "Famous player: Magic Johnson, Stephen Curry, Chris Paul"
    },
    "2": {
        "position": "SG (Score Guard)",
        "video": "https://www.youtube.com/embed/wb_qC3ZcCyw",
        "courtPosition": "https://i.ibb.co/n8bv1Dt/SG-position.jpg",
        "courtMoveMap": "https://i.ibb.co/S752SnB/SG-movemap.jpg",
        "description": "Outside scorer of a team. Mainly responsible for running through half court and finding a space "
                       "to catch the ball and shot. In the viedo, look at No 11 player Klay Thompson shooting that "
                       "3 point ball! <br>"
                       "Famous Player: Michael Jordan, Kobe Bryant"
    },
    "3": {
        "position": "SF (Small Forward)",
        "video": "https://www.youtube.com/embed/uBgtirMRQFQ",
        "courtPosition": "https://i.ibb.co/pdpLj3T/SF-position.jpg",
        "courtMoveMap": "https://i.ibb.co/H75L9cB/SF-movemap.jpg",
        "description": "Score core of a team. Mainly responsible for multiple tasks including both inside and outside "
                       "offense/defense and sometimes rebound. In the video, look at No 7 player Kevin Durant dribbling"
                       " ball to the basket and finishing with a jump shot. <br>"
                       "Famous Player: Lebron James, Larry Bird, Kevin Durant"
    },
    "4": {
        "position": "PF (Power Forward)",
        "video": "https://www.youtube.com/embed/0tbWhV-PkIY",
        "courtPosition": "https://i.ibb.co/CJXZMnH/PF-position.jpg",
        "courtMoveMap": "https://i.ibb.co/SJcn5hD/PF-movemap.jpg",
        "description": "Inside defender of a team. Mainly responsible for scrambling rebound, picking and rolling "
                       "for PG, blocking opponent in paint area and other “dirty” and tiring work. In the video, look "
                       "at No 21 player Tim Duncan who defences opponents' inner player and give him a block at the "
                       "end. <br>"
                       "Famous player: Tim Duncan, Kevin Garnett"
    },
    "5": {
        "position": "C (Center)",
        "video": "https://www.youtube.com/embed/j_Chf5qBQPY?start=6",
        "courtPosition": "https://i.ibb.co/x2w0Jm9/C-position.jpg",
        "courtMoveMap": "https://i.ibb.co/pymk5tG/C-movemap.jpg",
        "description": "Inside core of a team. Mainly responsible for paint area offense, scrambling rebound and "
                       "defending insider opponent. In the video, look at No 12 player Dwight Howard that jumps high"
                       " while running to the basket, he catches the passed ball and finishes a dunk against "
                       "opponent! <br>"
                       "Famous player: Dwight Howard, Shaq O’Neal"
    },
    "6": {
        "video": "https://youtube.com/embed/4_4CymXARWQ",
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


# === Data =============================================================================================================
# Quiz data
num_of_quiz = 6
usr_choice = []
quiz_data = {
    0: {
        "position": "PG",
        "video": "https://www.youtube.com/embed/izzHABI1F2I?start=3",
        "courtMoveMap": "https://i.ibb.co/mFp1SMB/PG-movemap.jpg",
        "options": ["PG", "SG", "SF", "PF", "C"],
        "description": "Brain of a team. Mainly responsible for dribbling ball through the court, organizing tactic and"
                       " passing ball to teammate with space to shot. In the video, look at No 3 player Chirs Paul "
                       "dribbling ball from back-court to front court and throwing ball to teammate. "
                       "Famous player: Magic Johnson, Stephen Curry, Chris Paul"
    },
    1: {
        "position": "SG",
        "video": "https://www.youtube.com/embed/wb_qC3ZcCyw",
        "courtMoveMap": "https://i.ibb.co/S752SnB/SG-movemap.jpg",
        "options": ["PG", "SG", "SF", "PF", "C"],
        "description": "Outside scorer of a team. Mainly responsible for running through half court and finding a space"
                       " to catch the ball and shot. In the viedo, look at No 11 player Klay Thompson shooting that "
                       "3 point ball! "
                       "Famous Player: Michael Jordan, Kobe Bryant"
    },
    2: {
        "position": "SF",
        "video": "https://www.youtube.com/embed/uBgtirMRQFQ",
        "courtPosition": "https://i.ibb.co/pdpLj3T/SF-position.jpg",
        "courtMoveMap": "https://i.ibb.co/H75L9cB/SF-movemap.jpg",
        "options": ["PG", "SG", "SF", "PF", "C"],
        "description": "Score core of a team. Mainly responsible for multiple tasks including both inside and outside "
                       "offense/defense and sometimes rebound. In the video, look at No 7 player Kevin Durant dribbling"
                       " ball to the basket and finishing with a jump shot. "
                       "Famous Player: Lebron James, Larry Bird, Kevin Durant"
    },
    3: {
        "position": "PF",
        "video": "https://www.youtube.com/embed/0tbWhV-PkIY",
        "courtPosition": "https://i.ibb.co/CJXZMnH/PF-position.jpg",
        "courtMoveMap": "https://i.ibb.co/SJcn5hD/PF-movemap.jpg",
        "options": ["PG", "SG", "SF", "PF", "C"],
        "description": "Inside defender of a team. Mainly responsible for scrambling rebound, picking and rolling "
                       "for PG, blocking opponent in paint area and other “dirty” and tiring work. In the video, look "
                       "at No 21 player Tim Duncan who defences opponents' inner player and give him a block at the "
                       "end."
                       "Famous player: Tim Duncan, Kevin Garnett"
    },
    4: {
        "position": "C",
        "video": "https://www.youtube.com/embed/j_Chf5qBQPY?start=6",
        "courtPosition": "https://i.ibb.co/x2w0Jm9/C-position.jpg",
        "courtMoveMap": "https://i.ibb.co/pymk5tG/C-movemap.jpg",
        "options": ["PG", "SG", "SF", "PF", "C"],
        "description": "Inside core of a team. Mainly responsible for paint area offense, scrambling rebound and "
                       "defending insider opponent. In the video, look at No 12 player Dwight Howard that jumps high"
                       " while running to the basket, he catches the passed ball and finishes a dunk against opponent! "
                       "Famous player: Dwight Howard, Shaq O’Neal"
    },
    5: {
        "position": "Drag and drop",
    }
}
# init usr_choice
for i in range(num_of_quiz):
    usr_choice.append({'choice': "None", 'correct': "False"})


# === ROUTES ===========================================================================================================

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


# Quiz Routes
@application.route('/quiz/')
def quiz_start():
    '''
    Initial page to Start quiz
    '''
    global usr_choice
    usr_choice = []
    for i in range(num_of_quiz):
        usr_choice.append({'choice': "None", 'correct': "False"})
    return render_template('quiz_start.html')


@application.route('/quiz/<qid>')
def quiz(qid):
    '''
    Render quiz/<qid>
    qid: quiz id start from 0
    usr_choice: global var; usr_choice[qid] get user's choice for the qid
    quiz_data:
    '''
    global usr_choice
    global quiz_data

    qidInt = int(qid)

    if qidInt >= 0 and qidInt < len(usr_choice)-1:
        return render_template('quiz.html', qid=qid, usr_choice=usr_choice, quiz_data=quiz_data[qidInt])
    elif qidInt == len(usr_choice)-1:
        # drag and drop quiz
        # print(len(usr_choice)-1, "is user_choice")
        return render_template('quiz_last.html', qid=qid, usr_choice=usr_choice)


@application.route('/update_usr_choice/<qid>', methods=['POST'])
def update_usr_choice(qid):
    '''
    Ajax call to update global var usr_choice
    '''
    global usr_choice

    json_data = request.get_json()
    usr_choice[int(qid)]["choice"] = json_data["choice"]
    usr_choice[int(qid)]["correct"] = json_data["correct"]
    # print("type is ", type(json_data["choice"]))
    print("usr_choice", usr_choice)
    return jsonify(data=usr_choice)


@application.route('/quiz/score')
def quiz_score():
    '''
    Quiz score page
    Calculate score from usr_choice
    '''
    global usr_choice

    score = 0
    for choice in usr_choice:
        if choice["correct"] == "True" or choice["correct"] == "true":
            score += 1

    return render_template('quiz_score.html', score=score, usr_choice=usr_choice, quiz_data=quiz_data)


# === Main ===========================================================================================================

if __name__ == '__main__':
    application.run(debug=True)
