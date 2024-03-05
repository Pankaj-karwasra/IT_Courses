from django.db import models

class students(models.Model):
    description=models.TextField()
    image=models.ImageField(upload_to='testimonial')
    name=models.CharField(max_length=50)
    course=models.CharField(max_length=70)

