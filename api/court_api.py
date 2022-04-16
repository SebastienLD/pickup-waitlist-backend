import os
import sys
import json
from flask import request

from app import app, db
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from models.team.model import Team

@app.route('/court/get', methods=['POST'])
def court_get():
    data = request.get_json()
    teams = (
        db.session.query(Team)
            .filter_by(court=data["court"])
    )
    team_ids = []
    for team in teams.all():
        team_ids.append({"id": team.team_id})
    return json.dumps({
        "teamIds": team_ids
    })


@app.route('/court/join', methods=['POST'])
def court_join():
    data = request.get_json()
    team = (
        db.session.query(Team)
            .filter_by(team_id=data["teamId"])
    )
    team.update({"court": data["court"]})
    db.session.commit()
    team = team.first()
    return json.dumps({
        "gameId": str(team.team_id),
        "court": team.court,
    })


@app.route('/court/leave', methods=['POST'])
def court_leave():
    data = request.get_json()
    team = (
        db.session.query(Team)
            .filter_by(team_id=data["teamId"])
    )
    team.update({"court": None})
    db.session.commit()
    team = team.first()
    return json.dumps({
        "gameId": str(team.team_id),
        "court": team.court,
    })