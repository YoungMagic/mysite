import threading
import logging
import time
import traceback

from django.http import JsonResponse

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x

local = threading.local()
logger = logging.getLogger('tracer')


class RequestLogMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        request.time = time.time()

    @staticmethod
    def process_response(request, response):
        try:
            cost_time = time.time() - request.time
            logger.info("┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            logger.info(f"│path: {request.path}")
            logger.info(f"│method: {request.method}")
            logger.info(f"│query: {list(request.GET.items())}")
            logger.info(f"│body: {request.body}")
            result = response.content.decode('utf-8')
            logger.info(f"│response: {result}")
            logger.info(f"│time: {round(cost_time, 3)} s")
            logger.info("└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        except Exception:
            logger.warning("process response log error")

        return response

    @staticmethod
    def process_exception(exc):
        logger.exception(exc)
        return JsonResponse({'code': -10006, 'message': exc.args})