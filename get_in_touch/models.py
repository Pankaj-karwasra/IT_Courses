from django.db import models

class get_in_touch(models.Model):
    address=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    email=models.EmailField()
