from django.db import models

class Team(models.Model):
    image=models.ImageField(upload_to='team/')
    name=models.CharField(max_length=255)
    course=models.CharField(max_length=250)