from django.db import models
from django.urls import reverse

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True) # unique=True to make sure that the email is unique

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teachers:teacher_detail', args=(str(self.id)))

