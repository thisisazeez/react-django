from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    
    # def __init__(self):
    #     return self.title 