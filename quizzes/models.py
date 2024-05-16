from django.db import models
from lessons.models import Lesson

class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE) # create a many-to-one relationship with the Lesson model
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question