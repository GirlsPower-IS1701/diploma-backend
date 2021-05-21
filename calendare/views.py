import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from calendare.models import Academic_Calendar, Events
from calendare.serializers import AcademicCalendarSerializer, EventsSerializer


class AcademicCalendarApi(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AcademicCalendarSerializer

    def get(self, request, *args, **kwargs):
        calendar = Academic_Calendar.objects.all()
        serializer = self.serializer_class(calendar)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            calendare = Academic_Calendar(
                name = serializer.validated_data.get("name"),
                semester=serializer.validated_data.get("semester"),
                from_year=serializer.validated_data.get("from_year"),
                to_year=serializer.validated_data.get("to_year")
            )
            calendare.save()
            response_serializer = self.serializer_class(calendare)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class EventsApi(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventsSerializer

    def get(self, request, *args, **kwargs):
        events = Events.objects.all()
        serializer = self.serializer_class(events)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            event = Events(
                name = serializer.validated_data.get("name"),
                academic_calendar=Academic_Calendar.objects.get(pk=request.POST["academic_calendar_id"]),
                from_date=serializer.validated_data.get("from_date"),
                to_date=serializer.validated_data.get("to_date")
            )
            event.save()
            response_serializer = self.serializer_class(event)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
@permission_classes([IsAuthenticated, ])
def get_calendar_events(request):

    spring_events = []
    autumn_events = []
    current_year = datetime.datetime.now().year-1
    for event in Events.objects.filter(academic_calendar=Academic_Calendar.objects.get(from_year=current_year)):
        if event.semester == "Autumn":
            autumn_events.append(EventsSerializer(event).data)
        elif event.semester == "Spring":
            spring_events.append(EventsSerializer(event).data)

    return Response({"Autumn": autumn_events, "Spring": spring_events})