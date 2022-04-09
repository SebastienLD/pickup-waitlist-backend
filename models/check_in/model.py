from app import db
from ..base import Base

class CheckIn(Base):
    __tablename__ = 'check_in'
    check_in_id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer())
    created = db.Column(db.DateTime())
    waiting = db.Column(db.Boolean())