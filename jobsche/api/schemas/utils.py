import marshmallow as ma


class BaseSchema(ma.Schema):
    guid = ma.fields.UUID(dump_only=True)
    created_at = ma.fields.DateTime(dump_only=True)
    updated_at = ma.fields.DateTime(dump_only=True)
