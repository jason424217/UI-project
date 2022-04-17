from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import pandas as pd
import numpy as np

application = Flask(__name__)


# === Data =============================================================================================================
# Quiz data
num_of_quiz = 6
usr_choice = []
quiz_data = {
    0: {
        "position": "PG (Point Guard)",
        "video": "https://www.youtube.com/embed/izzHABI1F2I?start=3",
        "courtPosition": "https://i.ibb.co/pW6TPts/PG-position.jpg",
        "courtMoveMap": "https://i.ibb.co/mFp1SMB/PG-movemap.jpg",
        "description": "Brain of a team. Mainly responsible for dribbling ball through the court, organizing tactic and"
                       " passing ball to teammate with space to shot. "
                       "Famous player: Magic Johnson, Stephen Curry, Chris Paul"
    },
    1: {
        "position": "SG (Score Guard)",
        "video": "https://www.youtube.com/embed/wb_qC3ZcCyw",
        "courtPosition": "https://i.ibb.co/n8bv1Dt/SG-position.jpg",
        "courtMoveMap": "https://i.ibb.co/S752SnB/SG-movemap.jpg",
        "description": "Outside scorer of a team. Mainly responsible for running through half court and finding a space "
                       "to catch the ball and shot."
                       "Famous Player: Michael Jordan, Kobe Bryant"
    },
    2: {
        "position": "SF (Small Forward)",
        "video": "https://www.youtube.com/embed/uBgtirMRQFQ",
        "courtPosition": "https://i.ibb.co/pdpLj3T/SF-position.jpg",
        "courtMoveMap": "https://i.ibb.co/H75L9cB/SF-movemap.jpg",
        "description": "Score core of a team. Mainly responsible for multiple tasks including both inside and outside "
                       "offense/defense and sometimes rebound."
                       "Famous Player: Lebron James, Larry Bird, Kevin Durant"
    },
    3: {
        "position": "PF (Power Forward)",
        "video": "https://www.youtube.com/embed/0tbWhV-PkIY",
        "courtPosition": "https://i.ibb.co/CJXZMnH/PF-position.jpg",
        "courtMoveMap": "https://i.ibb.co/SJcn5hD/PF-movemap.jpg",
        "description": "Inside defender of a team. Mainly responsible for scrambling rebound, picking and rolling "
                       "for PG, blocking opponent in paint area and other “dirty” and tiring work. "
                       "Famous player: Tim Duncan, Kevin Garnett"
    },
    4: {
        "position": "C (Center)",
        "video": "https://www.youtube.com/embed/j_Chf5qBQPY?start=6",
        "courtPosition": "https://i.ibb.co/x2w0Jm9/C-position.jpg",
        "courtMoveMap": "https://i.ibb.co/pymk5tG/C-movemap.jpg",
        "description": "Inside core of a team. Mainly responsible for paint area offense, scrambling rebound and "
                       "defending insider opponent. "
                       "Famous player: Dwight Howard, Shaq O’Neal"
    },
    5: {
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
# init usr_choice
for i in range(num_of_quiz):
    usr_choice.append({'choice':None,'correct':False})


# === ROUTES ===========================================================================================================
@application.route('/')
def homepage():
    return render_template('homepage.html')


# Quiz Routes
@application.route('/quiz/')
def quiz_start():
    '''
    Initial page to Start quiz
    '''
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
        return render_template('quiz.html',qid=qid, usr_choice=usr_choice, quiz_data=quiz_data[qidInt])
    elif qidInt == len(usr_choice)-1:
        # drag and drop quiz
        print(len(usr_choice)-1, "is user_choice")
        return render_template('quiz_last.html',qid=qid, usr_choice=usr_choice)


@application.route('/update_usr_choice/<qid>', methods=['POST'])
def update_usr_choice(qid):
    '''
    Ajax call to update global var usr_choice
    '''
    pass
    # json_data = request.get_json()
    #
    # return jsonify(data = data)

@application.route('/quiz/score')
def quiz_score():
    '''
    Quiz score page
    Calculate score from usr_choice
    '''
    return render_template('quiz_score.html')


# === Main ===========================================================================================================
if __name__ == '__main__':
   application.run(debug = True)
