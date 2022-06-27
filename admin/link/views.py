from rest_framework import viewsets, status
from rest_framework.response import Response

from link.models import Link
from link.serializers import LinkSerializer
import uuid

from .producer import publish

class LinkViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['shorted_link'] = uuid.uuid4().hex[:10]
            serializer.save()
            publish('new_link', serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        list_of_links = Link.objects.all()
        serializer = LinkSerializer(list_of_links, many=True)
        return Response(serializer.data)
