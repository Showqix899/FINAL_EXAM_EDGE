from django.urls import path

from .views import EventView,EventListView,EventDeleteView,EventDetailsView,EvnetUpdateView

urlpatterns = [
    path('event-add/',EventView.as_view(),name="event-add"),
    path('event-list/',EventListView.as_view(),name='event-list'),
    path('event-delete/<int:pk>/',EventDeleteView.as_view(),name="event-delete"),
    path("event-update/<int:pk>/",EvnetUpdateView.as_view(),name='event-update'),
    path('event-details/',EventDetailsView.as_view(),name="event-details")

]
