import marshmallow as ma

from jobsche.api.schemas.utils import BaseSchema


class AppResponseSchema(BaseSchema):
    name = ma.fields.String(required=True)
    description = ma.fields.String(required=True)


class SecretKeyResponseSchema(ma.Schema):
    secret_key = ma.fields.UUID(required=True)
