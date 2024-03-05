from django.db import models

class categories(models.Model):
    title=models.CharField(max_length=250)
    number=models.IntegerField()
