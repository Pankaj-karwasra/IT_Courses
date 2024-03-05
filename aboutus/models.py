from django.db import models

class aboutus(models.Model):
    image=models.ImageField(upload_to="about/")
    title=models.CharField(max_length=255)
    description=models.TextField()
    subjects=models.IntegerField()
    course=models.IntegerField()
    instructor=models.IntegerField()
    students=models.IntegerField()
