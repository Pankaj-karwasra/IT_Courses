from django.db import models

# Create your models here.
class course_details(models.Model):
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to='detail/')
    description=models.TextField()
    instructor=models.TextField(max_length=250)
    rating=models.FloatField()
    lecture=models.IntegerField()
    duration=models.FloatField()
    skill=models.CharField(max_length=250)
    language=models.CharField(max_length=250)
    price=models.IntegerField()