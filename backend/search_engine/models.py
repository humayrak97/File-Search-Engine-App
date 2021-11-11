from django.db import models

class People(models.Model):
    email = models.EmailField(max_length=200, unique = True, blank = False)
    pwd = models.CharField(max_length=100, default="", blank = False)
    #created_at = models.DateTimeField(auto_now_add = True)
