from django.urls import path

from . import views

urlpatterns = [
    path('reservations/', views.ReservationsListView.as_view()),
    path('reservations/<str:pk>/', views.ReservationsListView.as_view()),
    path('rooms/', views.RoomsListView.as_view()),
    path('rooms/<str:pk>/', views.RoomsListView.as_view())
]