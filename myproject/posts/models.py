from django.db import models

class post(models.Model):
    title = models.TextField()
    description = models.TextField()