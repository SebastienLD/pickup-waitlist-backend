from datetime import datetime
import os
import sys
import json
from flask import request
import uuid
import logging

from app import app, db
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from models.team.model import Team
from models.player.model import Player

@app.route('/team/list', methods=['GET'])
def team_list():
    teams = (
        db.session.query(Team).all()
    )
    team_ids = []
    for team in teams:
        team_ids.append({"id": str(team.team_id), "court": team.court})
    return json.dumps({
        "teamIds": team_ids
    })

@app.route('/team/get', methods=['POST'])
def team_get():
    data = request.get_json()
    team = (
        db.session.query(Team)
            .filter_by(team_id=data["teamId"])
    ).first()
    num_team_members = (
        db.session.query(Player)
            .filter_by(team_id=data["teamId"]).count()
    )
    return json.dumps({
        "teamId": str(team.team_id),
        "teamName": team.team_name,
        "created": str(datetime.timestamp(team.created)),
        "court": team.court,
        "members": num_team_members
    })

@app.route('/team/all/get', methods=['GET'])
def team_all_get():
    teams = db.session.query(Team).all()
    teamArray = list()
    for team in teams:
        players = (
            db.session.query(Player)
                .filter_by(team_id=team.team_id).all()
        )
        playerArray = list()
        for player in players:
            playerArray.append({
                "playerId": str(player.player_id),
                "teamId": str(player.team_id),
                "name": player.name,
                "created": str(datetime.timestamp(player.created)),
            })
        teamArray.append({
            "teamId": str(team.team_id),
            "teamName": team.team_name,
            "created": str(datetime.timestamp(team.created)),
            "court": team.court,
            "players": playerArray
        })
    return json.dumps({
        "teamArray": teamArray
    })

@app.route('/team/join', methods=['POST'])
def team_join():
    data = request.get_json()
    player = (
        db.session.query(Player)
            .filter_by(player_id=data["playerId"])
    )
    player.update({"team_id": data["teamId"]})
    db.session.commit()
    player = player.first()
    return json.dumps({
        "playerId": str(player.player_id),
        "teamId": str(player.team_id),
    })

@app.route('/team/leave', methods=['POST'])
def team_leave():
    data = request.get_json()
    player = (
        db.session.query(Player)
            .filter_by(player_id=data["playerId"]).first()
    )
    old_team_id = player.team_id
    player.team_id = None
    db.session.commit()
    players_in_team = (
        db.session.query(Player)
            .filter_by(team_id=old_team_id).count()
    )
    if players_in_team == 0:
        team = db.session.query(Team).get(old_team_id)
        db.session.delete(team)
        db.session.commit()

    return json.dumps({
        "playerId": str(player.player_id),
        "teamId": str(player.team_id),
    })

@app.route('/team/create', methods=['POST'])
def team_create():
    data = request.get_json()
    team_name_number = 1
    teams = db.session.query(Team).all()
    if teams:
        latest_team = max(teams, key=lambda x: x.created)
        team_name_number = int(latest_team.team_name.split()[1]) + 1
        if team_name_number >= 100:
            team_name_number = 1

    new_team = Team(
        team_id=str(uuid.uuid4()),
        team_name=f"Team {team_name_number}",
        court=data["court"],
        created=datetime.fromtimestamp(float(data["created"])),
    )
    db.session.add(new_team)
    player = (
        db.session.query(Player)
            .filter_by(player_id=data["playerId"]).first()
    )
    player.team_id = str(new_team.team_id)
    db.session.commit()
    return json.dumps({
        "teamId": str(new_team.team_id),
        "teamName": new_team.team_name,
        "created": str(datetime.timestamp(new_team.created)),
    })