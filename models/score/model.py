from app import db
from ..base import Base

class Score(Base):
    __tablename__ = 'score'
    score_id = db.Column(db.Integer(), primary_key=True)
    game_id = db.Column(db.Integer())
    team_id = db.Column(db.Integer())
    score = db.Column(db.Integer())