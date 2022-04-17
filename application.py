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
        "position": "PG",
        "video": "https://www.youtube.com/embed/izzHABI1F2I?start=3",
        "courtMoveMap": "https://i.ibb.co/mFp1SMB/PG-movemap.jpg",
        "options": ["PG","SG","SF","PF","C"]
    },
    1: {
        "position": "SG",
        "video": "https://www.youtube.com/embed/wb_qC3ZcCyw",
        "courtMoveMap": "https://i.ibb.co/S752SnB/SG-movemap.jpg",
        "options": ["PG","SG","SF","PF","C"]
    },
    2: {
        "position": "SF",
        "video": "https://www.youtube.com/embed/uBgtirMRQFQ",
        "courtPosition": "https://i.ibb.co/pdpLj3T/SF-position.jpg",
        "courtMoveMap": "https://i.ibb.co/H75L9cB/SF-movemap.jpg",
        "options": ["PG","SG","SF","PF","C"]
    },
    3: {
        "position": "PF",
        "video": "https://www.youtube.com/embed/0tbWhV-PkIY",
        "courtPosition": "https://i.ibb.co/CJXZMnH/PF-position.jpg",
        "courtMoveMap": "https://i.ibb.co/SJcn5hD/PF-movemap.jpg",
        "options": ["PG","SG","SF","PF","C"]
    },
    4: {
        "position": "C",
        "video": "https://www.youtube.com/embed/j_Chf5qBQPY?start=6",
        "courtPosition": "https://i.ibb.co/x2w0Jm9/C-position.jpg",
        "courtMoveMap": "https://i.ibb.co/pymk5tG/C-movemap.jpg",
        "options": ["PG","SG","SF","PF","C"]
    }
}
# init usr_choice
for i in range(num_of_quiz):
    usr_choice.append({'choice':"None",'correct':"False"})


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
    global usr_choice
    usr_choice = []
    for i in range(num_of_quiz):
        usr_choice.append({'choice':"None",'correct':"False"})
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
        # print(len(usr_choice)-1, "is user_choice")
        return render_template('quiz_last.html',qid=qid, usr_choice=usr_choice)

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
    print("usr_choice",usr_choice)
    return jsonify(data = usr_choice)

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
            score+=1

    return render_template('quiz_score.html', score=score, usr_choice=usr_choice)


# === Main ===========================================================================================================
if __name__ == '__main__':
   application.run(debug = True)
