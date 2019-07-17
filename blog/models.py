from django.db import models

class Stories(models.Model):
    title= models.TextField()
    content= models.TextField()