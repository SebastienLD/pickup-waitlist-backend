from app import db
from base import Base

class User(Base):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())