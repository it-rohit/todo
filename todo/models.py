from django.db import models

# Create your models here.
class Task (models.Model):
    task=models.CharField(max_length=500)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



    # string representation of models
    def __str__(self):
        return self.task