from django.http import HttpResponsePermanentRedirect
from rest_framework.views import APIView

from link.models import Link

from .producer import publish

class LinkViewSet(APIView):
    def get(self, request, *args, **kwargs):
        print(kwargs['shorted_link'])
        publish('web',{'shorted_link':kwargs['shorted_link']})
        link = Link.objects.filter(shorted_link=kwargs['shorted_link']).first()
        return HttpResponsePermanentRedirect(link.main_link)
