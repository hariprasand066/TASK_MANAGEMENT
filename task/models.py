from django.db import models

class User(models.Model):
    ROLE_CHOICES = (
        ('KM', 'Knowledge Manager'),
        ('Manager', 'Manager'),
    )
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.role})"

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_by = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='received_tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
