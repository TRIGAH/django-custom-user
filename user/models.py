from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


# Create your models here.

class User(AbstractUser):
    
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        TEACHER = "TEACHER", 'Teacher'
        STUDENT = "STUDENT", 'Student'

    base_role = Role.ADMIN        

    role = models.CharField(max_length=50, choices=Role.choices)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
        
class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)      