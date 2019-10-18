from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'objects', views.ObjectViewSet, basename='objects')

urlpatterns = [
    # url(r'^(?P<projectid>.*)/items/$', views.ItemsView.as_view()),
]

urlpatterns += router.urls
