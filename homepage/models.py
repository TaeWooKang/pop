from django.db import models

# Create your models here.

class Member(models.Model):
    user_id = models.CharField(max_length=30)
    user_pwd = models.CharField(max_length=30)
    user_nick = models.CharField(max_length=30)
    user_email = models.CharField(max_length=40)
    c_date = models.DateTimeField(null=True)