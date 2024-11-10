from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Event, RSVP
from .serializers import EventSerializer, RSVPSerializer

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class RSVPView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, event_id):
        event = Event.objects.get(id=event_id)
        rsvp, created = RSVP.objects.get_or_create(user=request.user, event=event)
        if created:
            return Response({'status': 'RSVP created'}, status=201)
        else:
            return Response({'status': 'Already RSVPed'}, status=400)

class UserRSVPsView(generics.ListAPIView):
    serializer_class = RSVPSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RSVP.objects.filter(user=self.request.user)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('event-list')  # Redirect to any page after signup
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
    
