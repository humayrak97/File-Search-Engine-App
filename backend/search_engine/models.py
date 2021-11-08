from django.db import models

class People(models.Model):
    email = models.CharField(max_length=300)
    passs = models.CharField(max_length=50)
