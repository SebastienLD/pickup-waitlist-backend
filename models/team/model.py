from app import db
from base import Base

class Team(Base):
    __tablename__ = 'team'
    team_id = db.Column(db.Integer(), primary_key=True)
    created = db.Column(db.Timestamp())