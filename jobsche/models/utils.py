from datetime import datetime
from uuid import uuid4
from jobsche.db import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(
        db.String(36),
        unique=True,
        index=True,
        default=lambda: str(uuid4()),
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    def save(self):
        if self.id is None and self.guid:
            raise ValueError('Cannot save an object with a guid')

        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
