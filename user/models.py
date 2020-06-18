from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractUser)

# Create your models here.
class CustomUserManager(BaseUserManager):
    pass

class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=20)
    description = models.CharField(max_length=50,null=True)

# User 表, 保存用户信息
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    account = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=20)
