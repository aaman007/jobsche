from jobsche.db import db
from jobsche.models.utils import BaseModel


class App(BaseModel):
    __tablename__ = 'apps'

    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.TEXT, nullable=True)
    secret_key = db.Column(db.String(32), nullable=True, index=True)

    def __repr__(self):
        return f'<App: {self.name}>'
