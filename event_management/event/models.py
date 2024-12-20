from django.db import models

# Create your models here.

class Event(models.Model):

    status_options=[('upcomming','upcomming'),('ongoing','ongoing'),('completed','completed')]

    title=models.CharField(max_length=150,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    location=models.CharField(max_length=200,null=True,blank=True)
    date_time=models.DateTimeField()
    capacity=models.IntegerField()
    status=models.CharField(max_length=30,null=True,blank=True)


    def __str__(self):

        return self.title
    

