from datetime import datetime
from feathr_bot.exceptions.errors import FeathrBotSqlAlchemyError
from feathr_bot.extensions import db


class BaseModel(db.Model):
    """Base SQLAlchemy model"""

    __abstract__ = True

    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    deleted_on = db.Column(db.DateTime)

    def save(self) -> db.Model:
        """persist model"""
        db.session.add(self)
        try:
            db.session.commit()
            return self
        except Exception as e:
            db.session.rollback()
            raise FeathrBotSqlAlchemyError(description=str(e))
