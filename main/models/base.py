from datetime import datetime

from main import db


class BaseModel(db.Model):
    """Base model for all models"""

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __str__(self) -> str:
        return f"<BaseModel {self.id}>"
