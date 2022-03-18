from uuid import uuid4

from jobsche.db import db
from jobsche.models.utils import BaseModel


class App(BaseModel):
    __tablename__ = 'apps'

    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.TEXT, nullable=True)
    secret_key = db.Column(db.String(36), nullable=False)

    def __repr__(self):
        return f'<App: {self.name}>'

    def save(self):
        if not self.id:
            self.secret_key = uuid4()
        super().save()
