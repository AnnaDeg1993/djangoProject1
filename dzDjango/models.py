from django.db import models


class ModelAnna(models.Model):
    pole = models.TextField()
    email = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
