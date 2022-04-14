import uuid
from app import db
from ..base import Base
from sqlalchemy.dialects.postgresql import UUID


class Player(Base):
    __tablename__ = 'player'
    player_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ##user_id = db.Column(db.Integer())
    team_id = db.Column(UUID(as_uuid=True))
    name = db.Column(db.String())
    created = db.Column(db.DateTime())