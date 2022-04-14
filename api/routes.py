from datetime import datetime
import os
import sys
from flask import request

from app import app, db
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
# from models.check_in.model import CheckIn
from models.team.model import Team
from models.player.model import Player

# @app.route('/check_in', methods=['POST'])
# def check_in():
#     data = request.get_json()
#     db.session.add(
#         CheckIn(
#             user_id=data["userId"],
#             created=datetime.now(),
#             waiting=True,
#         )
#     )
#     return {}

@app.route('/call_next')
def call_next():
    #data = request.get_json()
    new_team = Team(created=datetime.now())
    #player_name=data["name"]
    player_name = "Sebastien"
    new_player = Player(name=player_name, team_id=new_team.team_id)
    
    db.session.add_all([new_team, new_player])
    db.session.commit()
    return f'You called next!'

@app.route('/join_team', methods=['POST'])
def join_team():
    data = request.get_json()
    new_player = Player(name=data["name"], team_id=data["teamId"])
    
    db.session.add(new_player)
    db.session.commit()
    return {}

@app.route('/test')
def test():
    return 'Hello World! I am from docker!'
