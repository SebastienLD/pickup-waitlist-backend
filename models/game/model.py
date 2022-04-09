from app import db
from ..base import Base

class Game(Base):
    __tablename__ = 'game'
    id = db.Column(db.Integer(), primary_key=True)
    court = db.Column(db.Integer())
    team1_id = db.Column(db.Integer())
    team2_id = db.Column(db.Integer())