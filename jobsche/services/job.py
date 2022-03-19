from jobsche.models.job import (
    RegularJob,
    DelayedJob,
    ScheduledJob,
    RecurrentJob,
)
from jobsche.services.utils import BaseService


class RegularJobService(BaseService):
    _model = RegularJob


class DelayedJobService(BaseService):
    _model = DelayedJob


class ScheduledJobService(BaseService):
    _model = ScheduledJob


class RecurrentJobService(BaseService):
    _model = RecurrentJob
