from django.db import models

class Sport(models.Model):
    
    name = models.CharField(max_lenght=100)
    
