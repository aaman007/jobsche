import marshmallow as ma

from jobsche.api.schemas.utils import BaseSchema


class BaseJobSchema(BaseSchema):
    status = ma.fields.String(dump_only=True)
    retries = ma.fields.Integer(required=True)
    backoff_delay = ma.fields.Integer(required=True)
    backoff_fixed = ma.fields.Boolean(required=True)
    lambda_webhook_url = ma.fields.String(required=True)
    result_webhook_url = ma.fields.String(required=True)


class RegularJobSchema(BaseJobSchema):
    pass


class DelayedJobSchema(BaseJobSchema):
    countdown = ma.fields.Integer(required=True)


class ScheduledJobSchema(BaseJobSchema):
    scheduled_at = ma.fields.DateTime(required=True)


class RecurrentJobSchema(BaseJobSchema):
    cron_rule = ma.fields.String(required=True)
