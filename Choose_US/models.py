from django.db import models

class Choose_US(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
