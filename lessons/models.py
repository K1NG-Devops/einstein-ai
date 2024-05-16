from django.db import models
from teachers.models import Teacher
from students.models import Student

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE) # create a many-to-one relationship with the Teacher model

    def __str__(self):
        return self.title