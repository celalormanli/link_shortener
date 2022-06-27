from django.urls import path
from link.views import LinkViewSet

urlpatterns = [
    path('<str:shorted_link>/', LinkViewSet.as_view()),
]
