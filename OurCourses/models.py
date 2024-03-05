from django.db import models

class OurCourses(models.Model):
    image=models.ImageField(upload_to='course/')
    title=models.CharField(max_length=255)
    instructor=models.CharField(max_length=255)
    rating=models.FloatField(default=0.0)
    num_reviws=models.IntegerField(default=0)
    views=models.IntegerField(default=0)
