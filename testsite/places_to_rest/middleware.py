import datetime

from places_to_rest.models import UsersActivity


class TestMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            UsersActivity(user_id=request.user.id, user_name=request.user, request_method=request.method,
                          request_date=datetime.datetime.now()).save()
        print(request.user.id)
        print(request.user)
        print(request.method)
        print(datetime.datetime.now())
        response = self._get_response(request)
        return response
