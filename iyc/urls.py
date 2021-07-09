from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('events/', views.EventList.as_view(), name='event_list'),
    path('events/<int:pk>', views.EventDetail.as_view(), name='event_detail'),
]
