from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        TEACHER = "TEACHER", 'Teacher'
        STUDENT = "STUDENT", 'Student'

    base_role = Role.ADMIN        

