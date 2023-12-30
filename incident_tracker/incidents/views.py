from rest_framework import generics
from .models import Incident
from .serializers import IncidentSerializer
from django.shortcuts import render
from django.views import View

class IncidentList(generics.ListCreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class IncidentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer


class IncidentListView(View):
    template_name = 'incidents/incident_list.html'

    def get(self, request):
        incidents = Incident.objects.all()
        return render(request, self.template_name, {'incidents': incidents})