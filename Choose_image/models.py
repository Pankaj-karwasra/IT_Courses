from django.db import models

class Choose_image(models.Model):
    image=models.ImageField(upload_to="feature/")
