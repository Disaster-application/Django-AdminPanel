from django.db import models

# Create your models here.
class admin_login(models.Model):

    username = models.CharField(max_length=12)
    user_pass = models.CharField(max_length=12)
    remember_me = models.BooleanField(default=False)

class sendAlert(models.Model):
    alertMsg = models.CharField(max_length=100)
    alertType = models.CharField(max_length=100)
    alertTime = models.DateField(auto_created=True)