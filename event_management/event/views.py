from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView,DestroyAPIView,UpdateAPIView
from .models import Event
from .serializers import EventSerializer





class EventView(APIView):


    #add a new event
    def post(self, request):
        data = request.data
        serializer = EventSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EventListView(ListAPIView):

    queryset=Event.objects.all()
    serializer_class=EventSerializer



class EventDeleteView(DestroyAPIView):

    queryset=Event.objects.all()
    serializer_class=EventSerializer()


class EvnetUpdateView(UpdateAPIView):

    queryset=Event.objects.all()
    serializer_class=EventListView




class EventDetailsView(APIView):

    def get(self,request,pk):

        try:
            event=Event.objects.filter(id=pk)

            serialzer=EventSerializer(event,data=request.data)
            if serialzer.is_valid():
                return Response("success")
        except Event.DoesNotExist:
            return Response("does not exist")
