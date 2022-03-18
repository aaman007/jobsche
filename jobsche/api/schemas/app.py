import marshmallow as ma

from jobsche.api.schemas.utils import BaseSchema


class AppSchema(BaseSchema):
    name = ma.fields.String(required=True)
    description = ma.fields.String(required=True)
