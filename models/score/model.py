from app import db

class Score(db.Model):
    __tablename__ = 'score'
    score_id = db.Column(db.Integer(), primary_key=True)
    game_id = db.Column(db.Integer())
    team_id = db.Column(db.Integer())
    score = db.Column(db.Integer())