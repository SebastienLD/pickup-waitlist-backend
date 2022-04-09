from app import db

class CheckIn(db.Model):
    __tablename__ = 'check_in'
    check_in_id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer())
    created = db.Column(db.Timestamp())
    waiting = db.Column(db.Boolean())