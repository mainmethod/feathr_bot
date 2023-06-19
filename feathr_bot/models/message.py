""" Message model """
from feathr_bot.extensions import db
from feathr_bot.models.base import BaseModel


class Message(BaseModel):
    """SQLAlchemy model for Messages"""

    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey("chat.id"))
    role = db.Column(db.String)
    content = db.Column(db.String)
    chat = db.relationship("Chat", lazy="joined")
