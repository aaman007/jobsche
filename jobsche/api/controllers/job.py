from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from jobsche.api.controllers.utils import (
    safe_service_call,
    authorized_app
)
from jobsche.api.schemas.job import (
    RegularJobSchema,
    DelayedJobSchema,
    ScheduledJobSchema,
    RecurrentJobSchema,
    JobQueryArgsSchema,
)
from jobsche.services.job import (
    RegularJobService,
    DelayedJobService,
    ScheduledJobService,
    RecurrentJobService,
)


blp = Blueprint(
    'job',
    __name__,
    url_prefix='/api/job',
    description='Job related operations',
)


@blp.route('/delay')
class RegularJobCreateView(MethodView):

    @blp.arguments(RegularJobSchema, location='json')
    @blp.response(201, RegularJobSchema)
    @authorized_app()
    def post(self, data):
        data['app_id'] = request.app.id
        return safe_service_call(
            RegularJobService.create,
            data,
        )


@blp.route('/countdown')
class DelayedJobCreateView(MethodView):

    @blp.arguments(DelayedJobSchema, location='json')
    @blp.response(201, DelayedJobSchema)
    @authorized_app()
    def post(self, data):
        data['app_id'] = request.app.id
        return safe_service_call(
            DelayedJobService.create,
            data,
        )


@blp.route('/schedule')
class ScheduledJobCreateView(MethodView):

    @blp.arguments(ScheduledJobSchema, location='json')
    @blp.response(201, ScheduledJobSchema)
    @authorized_app()
    def post(self, data):
        data['app_id'] = request.app.id
        return safe_service_call(
            ScheduledJobService.create,
            data,
        )


@blp.route('/recur')
class RecurrentJobCreateView(MethodView):

    @blp.arguments(RecurrentJobSchema, location='json')
    @blp.response(201, RecurrentJobSchema)
    @authorized_app()
    def post(self, data):
        data['app_id'] = request.app.id
        return safe_service_call(
            RecurrentJobService.create,
            data,
        )


@blp.route('/<uuid:guid>')
class JobRetrieveView(MethodView):

    @staticmethod
    def _get_service(job_type):
        if job_type == 'delayed':
            return DelayedJobService
        elif job_type == 'scheduled':
            return ScheduledJobService
        elif job_type == 'recurrent':
            return RecurrentJobService
        elif job_type == 'delayed':
            return DelayedJobService
        return abort(500, 'Something went wrong!')

    @blp.arguments(JobQueryArgsSchema, location='query')
    @blp.response(200, RegularJobSchema)
    @authorized_app()
    def get(self, query, guid):
        service = self._get_service(query.get('type'))
        print(service, query)
        job = safe_service_call(
            service.find_by_guid,
            guid,
        )
        if job.app != request.app:
            abort(403, message='You do not have access to this job')
        return job
