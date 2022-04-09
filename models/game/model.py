from app import db

class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer(), primary_key=True)
    court = db.Column(db.Integer())
    team1_id = db.Column(db.Integer())
    team2_id = db.Column(db.Integer())