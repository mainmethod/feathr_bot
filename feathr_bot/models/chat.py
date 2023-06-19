""" Chat model """
from feathr_bot.extensions import db
from feathr_bot.models.base import BaseModel


class Chat(BaseModel):
    """SQLAlchemy model for Chats"""

    __tablename__ = "chat"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    messages = db.relationship(
        "Message",
        back_populates="chat",
        lazy="joined",
        order_by="Message.created_on.asc()",
    )
