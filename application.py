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
quiz_data = []
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
        return render_template('quiz.html',qid=qid, usr_choice=usr_choice)
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
