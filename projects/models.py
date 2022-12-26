from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.TextField()
    description = models.TextField()
    title = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    strength = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

