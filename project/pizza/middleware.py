from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout
import time

TIMEOUT = 30


class UserDisconnectionTimeMiddleware(MiddlewareMixin):

    def process_request(self, request):
        user_activity_time = request.session.get('user_activity_time')
        time_now = time.time()

        if user_activity_time:
            duration = time_now - user_activity_time
        else:
            duration = 0

        if duration > TIMEOUT:
            logout(request)
        else:
            request.session['user_activity_time'] = time_now

    def process_response(self, request, response):
        return response
