import uuid
from app import db
from sqlalchemy.dialects.postgresql import UUID
from ..base import Base

class Team(Base):
    __tablename__ = 'team'
    team_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    team_name = db.Column(db.String())
    court = db.Column(db.Integer())
    created = db.Column(db.DateTime())