from datetime import datetime
from flask import request

from app import app, db
from models.check_in import CheckIn
from models.team import Team
from models.player import Player

@app.route('/check_in', methods=['POST'])
def check_in():
    data = request.get_json()
    db.session.add(
        CheckIn(
            user_id=data["userId"],
            created=datetime.now(),
            waiting=True,
        )
    )
    return {}

@app.route('/call_next', methods=['POST'])
def check_in():
    data = request.get_json()
    new_team = Team(created=datetime.now())
    new_player = Player(name=data["name"], team_id=new_team.team_id)
    
    db.session.add_all([new_team, new_player])
    db.session.commit()
    return {}

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

@app.route('/test_db')
def test_db():
    db.create_all()
    db.session.commit()
    user = User.query.first()
    if not user:
        u = User(name='Mudasir', surname='Younas')
        db.session.add(u)
        db.session.commit()
    user = User.query.first()
    return "User '{} {}' is from database".format(user.name, user.surname)