from django.db import models

class Question(models.Model):
    name = models.CharField(max_length=255)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.name
