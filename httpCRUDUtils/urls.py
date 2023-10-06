from django.urls import path
from . import views

urlpatterns = [
    path('', views.RequestHandler.as_view(), name='request_handler'),
]
