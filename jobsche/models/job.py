from enum import Enum
from jobsche.db import db
from jobsche.models.utils import BaseModel


class JobStatus(Enum):
    SCHEDULED = 0
    RUNNING = 1
    EXECUTED = 2
    FAILED = 3


class BaseJob(BaseModel):
    __abstract__ = True

    status = db.Column(db.Enum(JobStatus), default=JobStatus.SCHEDULED)
    retries = db.Column(db.Integer, default=0)
    attempts = db.Column(db.Integer, default=0)
    backoff_delay = db.Column(db.Integer, default=0)
    backoff_fixed = db.Column(db.Boolean, default=True)
    lambda_webhook_url = db.Column(db.String(150), nullable=False)
    result_webhook_url = db.Column(db.String(150), nullable=False)


class RegularJob(BaseJob):
    __tablename__ = 'regular_jobs'

    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'), nullable=False)
    app = db.relationship('App', backref=db.backref('regular_jobs', lazy=True))


class DelayedJob(BaseJob):
    __tablename__ = 'delayed_jobs'

    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'), nullable=False)
    app = db.relationship('App', backref=db.backref('delayed_jobs', lazy=True))
    countdown = db.Column(db.Integer, nullable=False)


class ScheduledJob(BaseJob):
    __tablename__ = 'scheduled_jobs'

    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'), nullable=False)
    app = db.relationship(
        'App',
        backref=db.backref(
            'scheduled_jobs',
            lazy=True
        )
    )
    scheduled_at = db.Column(db.DateTime, nullable=False)


class RecurrentJob(BaseJob):
    __tablename__ = 'recurrent_jobs'

    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'), nullable=False)
    app = db.relationship(
        'App',
        backref=db.backref(
            'recurrent_jobs',
            lazy=True
        )
    )
    cron_rule = db.Column(db.String(30), nullable=False)
