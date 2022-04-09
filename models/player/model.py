from app import db

class Player(db.Model):
    __tablename__ = 'player'
    player_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer())
    team_id = db.Column(db.Integer())