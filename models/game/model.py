import uuid
from app import db
from ..base import Base
from sqlalchemy.dialects.postgresql import UUID


class Game(Base):
    __tablename__ = 'game'
    player_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    court = db.Column(db.Integer())
    team_one_id = db.Column(UUID(as_uuid=True))
    team_two_id = db.Column(UUID(as_uuid=True))
    over = db.Column(db.Boolean())
