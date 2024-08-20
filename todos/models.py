from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    rewards_for_completion = models.IntegerField(null=True, blank=True)
    STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    ('deferred', 'Deferred'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    

    def __str__(self):
        return self.title
