from app import db

class Team(db.Model):
    __tablename__ = 'team'
    team_id = db.Column(db.Integer(), primary_key=True)
    created = db.Column(db.Timestamp())