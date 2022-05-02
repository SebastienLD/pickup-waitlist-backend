from datetime import datetime
import os
import sys
import json
from flask import request
import uuid

from app import app, db
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from models.player.model import Player


@app.route('/player/get', methods=['POST'])
def player_get():
    data = request.get_json()
    player = (
        db.session.query(Player).
            filter_by(player_id=data["playerId"])
    ).first()
    return json.dumps({
        "playerId": str(player.player_id),
        "teamId": str(player.team_id),
        "name": player.name,
        "created": str(datetime.timestamp(player.created))
    })

@app.route('/player/create', methods=['POST'])
def player_create():
    data = request.get_json()
    new_player = Player(
        player_id=str(uuid.uuid4()),
        name=data["playerName"],
        created=datetime.fromtimestamp(float(data["created"])),
    )
    db.session.add(new_player)
    db.session.commit()
    return json.dumps({
        "playerId": str(new_player.player_id),
        "created": str(datetime.timestamp(new_player.created)),
    })

@app.route('/player/team', methods=['POST'])
def player_team():
    data = request.get_json()
    player = (
        db.session.query(Player)
            .filter_by(player_id=data["playerId"])
    ).first()
    return json.dumps({
        "playerId": str(player.player_id),
        "teamId": str(player.team_id),
    })