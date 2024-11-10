from django.urls import path
from .views import EventListView, RSVPView, UserRSVPsView, signup_view

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:event_id>/rsvp/', RSVPView.as_view(), name='rsvp-create'),
    path('user/rsvps/', UserRSVPsView.as_view(), name='user-rsvps'),
    path('signup/', signup_view, name='signup'),
]
