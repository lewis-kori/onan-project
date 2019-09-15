from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class accounts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("accounts:index")
    