from django.urls import path
from link.views import LinkViewSet

urlpatterns = [
      path('', LinkViewSet.as_view({'get': 'list', 'post': 'create'}), name='link-list'),
]
