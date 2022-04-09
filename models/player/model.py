from app import db
from ..base import Base

class Player(Base):
    __tablename__ = 'player'
    player_id = db.Column(db.Integer, primary_key=True)
    ##user_id = db.Column(db.Integer())
    team_id = db.Column(db.Integer())
    name = db.Column(db.String())