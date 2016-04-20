from django.db import models

# Create your models here.

class noticias(models.Model):
    titulo = models.TextField(primary_key=True)
    link = models.TextField()
