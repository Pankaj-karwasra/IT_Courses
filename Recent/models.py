from django.db import models

class Recent(models.Model):
    image=models.ImageField(upload_to='detail/')
    title=models.CharField(max_length=250)
    name=models.CharField(max_length=250)
    rating=models.IntegerField()
    number=models.IntegerField()

