from rest_framework import serializers


from datetime import date
from django.utils import timezone
from .models import Event

class EventSerializer(serializers.ModelSerializer):

    class Meta:

        model=Event
        fields='__all__'
        ordering=['-date_time']


    def validate(self, data):

        date_time=data.get('date_time')

        if date_time<timezone.now():

            raise serializers.ValidationError("invalid date and time")
        
        return super().validate(data)
        
    
    def create(self, validated_data):

        
        
        if validated_data['date_time']<timezone.now():

            validated_data['status']='completed'
        
        if validated_data['date_time']>timezone.now():

            validated_data['status']='upcomming'

        if validated_data['date_time']== timezone.now():

            validated_data['status']='on goinig'

        
        return super().create(validated_data)
        


        

        
