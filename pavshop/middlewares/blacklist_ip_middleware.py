from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin

class BlackListIPMiddleware(MiddlewareMixin):
    BLACK_IP_LIST=[
        '127.0.0.2',
    ]
    def process_request(self,request):
        if request.META.get('REMOTE_ADDR') in self.BLACK_IP_LIST:
            return HttpResponseForbidden("<h1>Olmaz!</h1>")