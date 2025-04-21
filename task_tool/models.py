from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_OPTION =[
    ('admin' ,'Admin'),
    ('KM','Key Manager'),
    ('manager','Manager'),
    ('tl', 'Team Lead'),
    ('employee', 'Employee')
]

class User(AbstractUser):
    role=models.CharField(max_length=20,choices=ROLE_OPTION)

    def _str_(self):
        return f"{self.username} ({self.role})"
    
class task(models.Model):
    task=models.CharField(max_length=120)
    assigned_to=models.ForeignKey(User,on_delete=models.CASCADE)
    Status=models.CharField(max_length=120)
    due_date=models.DateField()

    def __str__(self):
        return  self.task
