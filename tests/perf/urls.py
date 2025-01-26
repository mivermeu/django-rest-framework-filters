
from django.urls import include, re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'df-notes', views.DFNoteViewSet, basename='df-notes')
router.register(r'drf-notes', views.DRFFNoteViewSet, basename='drf-notes')


urlpatterns = [
    re_path(r'^', include(router.urls)),
]
