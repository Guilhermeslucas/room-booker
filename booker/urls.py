from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reservations/list', views.ReservationsListView.as_view()),
    path('rooms/list', views.RoomsListView.as_view())
]