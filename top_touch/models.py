from django.db import models

class top_touch(models.Model):
    phone=models.CharField(max_length=15)
    email=models.EmailField()
