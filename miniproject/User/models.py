from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length = 200, default="0000")
    is_leader = models.BooleanField(default=False)
    hearts = models.IntegerField(default=0)
