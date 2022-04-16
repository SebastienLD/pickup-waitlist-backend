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
from models.game.model import Game

@app.route('/game/list', methods=['POST'])
def game_list():
    data = request.get_json()
    active_games = (
        db.session.query(Game)
            .filter_by(over=False)
    )
    game_ids = []
    for game in active_games.all():
        game_ids.append({"id": str(game.game_id)})

    return json.dumps({
       "gameIds": game_ids
    })

@app.route('/game/create', methods=['POST'])
def game_create():
    data = request.get_json()
    new_game = Game(
        game_id=str(uuid.uuid4()),
        court=int(data["court"]),
        created=datetime.fromtimestamp(float(data["created"])),
    )
    db.session.add(new_game)
    db.session.commit()
    return json.dumps({
        "gameId": str(new_game.game_id),
        "created": str(datetime.timestamp(new_game.created)),
    })

@app.route('/game/join', methods=['POST'])
def game_join():
    data = request.get_json()
    game = (
        db.session.query(Game)
            .filter_by(game_id=data["gameId"])
    )
    if data["teamNumber"] == "one":
        game.update({"team_one_id": str(data["teamId"])})
    elif data["teamNumber" == "two"]:
        game.update({"team_two_id": str(data["teamId"])})
    
    db.session.commit()
    game = game.first()
    return json.dumps({
        "gameId": str(game.game_id),
        "teamNumber": data["teamNumber"],
        "teamId": data["teamId"],
    })


@app.route('/game/leave', methods=['POST'])
def game_leave():
    data = request.get_json()
    game = (
        db.session.query(Game)
            .filter_by(game_id=data["gameId"])
    )
    if data["teamNumber"] == "one":
        game.update({"team_one_id": None})
    elif data["teamNumber" == "two"]:
        game.update({"team_two_id": None})
    
    db.session.commit()
    game = game.first()
    return json.dumps({
        "gameId": str(game.game_id),
        "teamNumber": data["teamNumber"],
    })

@app.route('/game/end', methods=['POST'])
def game_end():
    data = request.get_json()
    game = (
        db.session.query(Game)
            .filter_by(game_id=data["gameId"])
    )
    game.update({"over": True})
    db.session.commit()
    game = game.first()
    return json.dumps({
        "gameId": str(game.game_id),
        "isOver": str(game.over),
    })

