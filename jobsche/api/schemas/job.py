import marshmallow as ma

from jobsche.api.schemas.app import AppSchema
from jobsche.api.schemas.utils import BaseSchema


class ChoiceField(ma.fields.Field):

    def __init__(self, *args, **kwargs):
        if 'choices' not in kwargs:
            raise ValueError('choices is required')
        super().__init__(*args, **kwargs)
        self.choices = kwargs.pop('choices')

    def _serialize(self, value, attr, obj, **kwargs):
        return value if value else ''

    def _deserialize(self, value, attr, data, **kwargs):
        mapper = {val: val for val in self.choices}
        try:
            return mapper[value]
        except KeyError as _:
            raise ma.ValidationError(f'Value must be one of: {self.choices}')


class JobQueryArgsSchema(ma.Schema):
    type = ChoiceField(
        choices=['regular', 'delayed', 'scheduled', 'recurrent'],
        required=True
    )


class BaseJobSchema(BaseSchema):
    app = ma.fields.Nested(AppSchema, dump_only=True)
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
