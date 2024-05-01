from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.CharField(max_length=50)
    introduction = models.TextField(blank=True, null=True)
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False)